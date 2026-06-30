#!/usr/bin/env python3
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Union
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_JSON = ROOT / "outputs/latest/crypto-market-signal.json"
OUTPUT_MD = ROOT / "outputs/latest/crypto-market-signal.md"

DEFAULT_SYMBOLS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT"]
SYMBOL_KEYWORDS = {
    "BTCUSDT": "bitcoin",
    "ETHUSDT": "ethereum",
    "BNBUSDT": "crypto_etf",
    "SOLUSDT": "crypto_etf",
    "XRPUSDT": "crypto_etf",
    "DOGEUSDT": "crypto_etf",
}
COINGECKO_IDS = {
    "bitcoin": ("BTCUSDT", "bitcoin"),
    "ethereum": ("ETHUSDT", "ethereum"),
    "binancecoin": ("BNBUSDT", "crypto_etf"),
    "solana": ("SOLUSDT", "crypto_etf"),
    "ripple": ("XRPUSDT", "crypto_etf"),
    "dogecoin": ("DOGEUSDT", "crypto_etf"),
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def fetch_json(url: str, timeout: int = 12) -> Union[dict, list]:
    request = Request(url, headers={"User-Agent": "investment-blog-operator/1.0"})
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def load_env_json(name: str) -> dict:
    value = os.getenv(name, "").strip()
    if not value:
        return {}
    try:
        candidate = Path(value)
        if candidate.exists():
            return json.loads(candidate.read_text())
    except OSError:
        pass
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return {}


def normalize_plugin_overview(raw: dict) -> dict:
    metrics = raw.get("metrics", {})
    fear_greed = metrics.get("fearGreedIndex", {})
    hot_tokens = raw.get("hotTokens", [])
    news = raw.get("analysis", {}).get("news", [])
    return {
        "available": bool(raw),
        "provider": "binance_plugin",
        "market_cap": metrics.get("marketCap", {}),
        "volume": metrics.get("volume", {}),
        "fear_greed": {
            "value": fear_greed.get("value"),
            "label": fear_greed.get("label", ""),
        },
        "hot_tokens": [
            {"symbol": item.get("symbol", ""), "name": item.get("name", "")}
            for item in hot_tokens
            if item.get("symbol")
        ][:12],
        "news": [
            {
                "category": item.get("category", ""),
                "summary": item.get("summary", ""),
                "publish_time_ts": item.get("publishTimeTs"),
            }
            for item in news
        ][:5],
    }


def fetch_fear_greed() -> dict:
    try:
        raw = fetch_json("https://api.alternative.me/fng/?limit=1")
        item = (raw.get("data") or [{}])[0]
        return {
            "value": int(item.get("value", 0)),
            "label": item.get("value_classification", ""),
            "source": "alternative.me",
            "timestamp": item.get("timestamp", ""),
        }
    except Exception as exc:  # noqa: BLE001
        return {"value": None, "label": "", "source": "alternative.me", "error": str(exc)}


def fetch_binance_tickers(symbols: list[str]) -> list[dict]:
    encoded = quote(json.dumps(symbols, separators=(",", ":")))
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbols={encoded}"
    try:
        raw = fetch_json(url)
    except Exception as exc:  # noqa: BLE001
        fallback_items = []
        fallback_errors = []
        for symbol in symbols:
            try:
                fallback_items.append(fetch_json(f"https://api.binance.com/api/v3/ticker/24hr?{urlencode({'symbol': symbol})}"))
            except Exception as fallback_exc:  # noqa: BLE001
                fallback_errors.append(f"{symbol}: {fallback_exc}")
        if fallback_items:
            raw = fallback_items
        else:
            return [{"error": str(exc), "fallback_errors": fallback_errors, "provider": "binance_public_api"}]

    tickers = []
    for item in raw:
        try:
            quote_volume = float(item.get("quoteVolume", 0))
            change_pct = float(item.get("priceChangePercent", 0))
            last_price = float(item.get("lastPrice", 0))
        except (TypeError, ValueError):
            quote_volume = 0.0
            change_pct = 0.0
            last_price = 0.0
        tickers.append(
            {
                "symbol": item.get("symbol", ""),
                "keyword": SYMBOL_KEYWORDS.get(item.get("symbol", ""), "crypto_etf"),
                "last_price": last_price,
                "price_change_percent_24h": change_pct,
                "quote_volume_24h": quote_volume,
                "trade_count_24h": int(item.get("count", 0) or 0),
            }
        )
    return sorted(tickers, key=lambda item: item.get("quote_volume_24h", 0), reverse=True)


def fetch_coingecko_tickers() -> list[dict]:
    ids = ",".join(COINGECKO_IDS)
    url = (
        "https://api.coingecko.com/api/v3/coins/markets"
        f"?vs_currency=usd&ids={ids}&order=volume_desc&per_page=20&page=1"
        "&sparkline=false&price_change_percentage=24h"
    )
    try:
        raw = fetch_json(url)
    except Exception as exc:  # noqa: BLE001
        return [{"error": str(exc), "provider": "coingecko_public_api"}]

    tickers = []
    for item in raw:
        symbol, keyword = COINGECKO_IDS.get(item.get("id", ""), (item.get("symbol", "").upper(), "crypto_etf"))
        try:
            last_price = float(item.get("current_price", 0) or 0)
            change_pct = float(item.get("price_change_percentage_24h", 0) or 0)
            quote_volume = float(item.get("total_volume", 0) or 0)
        except (TypeError, ValueError):
            last_price = 0.0
            change_pct = 0.0
            quote_volume = 0.0
        tickers.append(
            {
                "symbol": symbol,
                "keyword": keyword,
                "last_price": last_price,
                "price_change_percent_24h": change_pct,
                "quote_volume_24h": quote_volume,
                "trade_count_24h": 0,
                "provider": "coingecko_public_api",
            }
        )
    return sorted(tickers, key=lambda item: item.get("quote_volume_24h", 0), reverse=True)


def classify_market(fear_greed: dict, tickers: list[dict]) -> dict:
    valid = [item for item in tickers if "error" not in item]
    avg_change = round(sum(item.get("price_change_percent_24h", 0) for item in valid) / len(valid), 2) if valid else 0
    total_volume = round(sum(item.get("quote_volume_24h", 0) for item in valid), 2)
    fear_value = fear_greed.get("value")
    if isinstance(fear_value, int) and fear_value <= 25:
        sentiment = "extreme_fear"
    elif isinstance(fear_value, int) and fear_value >= 75:
        sentiment = "extreme_greed"
    elif avg_change <= -3:
        sentiment = "risk_off"
    elif avg_change >= 3:
        sentiment = "risk_on"
    else:
        sentiment = "mixed"

    signal_strength = 0
    if isinstance(fear_value, int):
        signal_strength += 3 if fear_value <= 25 or fear_value >= 75 else 1
    if abs(avg_change) >= 2:
        signal_strength += 2
    if total_volume > 0:
        signal_strength += 1

    return {
        "sentiment": sentiment,
        "average_change_percent_24h": avg_change,
        "tracked_quote_volume_24h": total_volume,
        "signal_strength": min(signal_strength, 6),
    }


def build_keyword_signals(plugin: dict, tickers: list[dict], market: dict, fear_greed: dict) -> dict:
    keyword_signals = {}
    for item in tickers:
        if "error" in item:
            continue
        keyword = item.get("keyword", "crypto_etf")
        current = keyword_signals.setdefault(
            keyword,
            {
                "signal_score_bonus": 0,
                "market_signal_notes": [],
                "tracked_symbols": [],
            },
        )
        current["tracked_symbols"].append(item["symbol"])
        if abs(item.get("price_change_percent_24h", 0)) >= 2:
            current["signal_score_bonus"] += 2
            current["market_signal_notes"].append(
                f"{item['symbol']} 24h change {item['price_change_percent_24h']:.2f}%"
            )
        if item.get("quote_volume_24h", 0) > 0:
            current["signal_score_bonus"] += 1

    if plugin.get("available"):
        hot_symbols = [item.get("symbol") for item in plugin.get("hot_tokens", []) if item.get("symbol")]
        if "BTC" in hot_symbols:
            keyword_signals.setdefault("bitcoin", {"signal_score_bonus": 0, "market_signal_notes": [], "tracked_symbols": []})
            keyword_signals["bitcoin"]["signal_score_bonus"] += 2
            keyword_signals["bitcoin"]["market_signal_notes"].append("Binance hot token carousel includes BTC")
        if "ETH" in hot_symbols:
            keyword_signals.setdefault("ethereum", {"signal_score_bonus": 0, "market_signal_notes": [], "tracked_symbols": []})
            keyword_signals["ethereum"]["signal_score_bonus"] += 2
            keyword_signals["ethereum"]["market_signal_notes"].append("Binance hot token carousel includes ETH")

    fear_value = fear_greed.get("value")
    if isinstance(fear_value, int):
        for keyword in ["bitcoin", "ethereum", "crypto_etf"]:
            current = keyword_signals.setdefault(
                keyword,
                {"signal_score_bonus": 0, "market_signal_notes": [], "tracked_symbols": []},
            )
            if fear_value <= 25:
                current["signal_score_bonus"] += 2
                current["market_signal_notes"].append(f"Fear/Greed {fear_value}: Extreme Fear zone")
            elif fear_value >= 75:
                current["signal_score_bonus"] += 2
                current["market_signal_notes"].append(f"Fear/Greed {fear_value}: Extreme Greed zone")

    for value in keyword_signals.values():
        value["signal_score_bonus"] = min(value["signal_score_bonus"], 8)
        value["market_sentiment"] = market.get("sentiment", "mixed")
    return keyword_signals


def render_md(payload: dict) -> str:
    lines = [
        "# Crypto Market Signal",
        "",
        f"- 생성 시각: `{payload['generated_at']}`",
        f"- 상태: `{payload['status']}`",
        f"- 시장 분위기: `{payload['market']['sentiment']}`",
        f"- 추적 코인 평균 24h 변동률: `{payload['market']['average_change_percent_24h']}%`",
        f"- Fear/Greed: `{payload['fear_greed'].get('value')}` ({payload['fear_greed'].get('label', '')})",
        "",
        "## Tracked Tickers",
        "",
    ]
    for item in payload.get("tickers", []):
        if "error" in item:
            lines.append(f"- Binance public API error: {item['error']}")
            continue
        lines.append(
            f"- `{item['symbol']}`: 24h `{item['price_change_percent_24h']:.2f}%`, "
            f"quote volume `{item['quote_volume_24h']:.0f}`"
        )
    lines.extend(["", "## Keyword Signals", ""])
    for keyword, signal in payload.get("keyword_signals", {}).items():
        lines.append(
            f"- `{keyword}`: bonus `{signal['signal_score_bonus']}`, "
            f"sentiment `{signal['market_sentiment']}`, symbols `{', '.join(signal.get('tracked_symbols', []))}`"
        )
        for note in signal.get("market_signal_notes", [])[:3]:
            lines.append(f"  - {note}")
    if payload.get("plugin_overview", {}).get("available"):
        lines.extend(["", "## Plugin Overview", ""])
        hot = payload["plugin_overview"].get("hot_tokens", [])
        lines.append(f"- Binance hot tokens: {', '.join(item['symbol'] for item in hot[:10])}")
    lines.extend(
        [
            "",
            "## Editorial Rule",
            "",
            "- 이 파일은 코인 글감의 시장 센서입니다. 투자 권유가 아니며, 규제/기업/ETF/기관 관련 문장은 별도 신뢰 소스로 교차 확인합니다.",
        ]
    )
    return "\n".join(lines).strip() + "\n"


def main() -> int:
    symbols = [item.strip().upper() for item in os.getenv("CRYPTO_SIGNAL_SYMBOLS", "").split(",") if item.strip()]
    if not symbols:
        symbols = DEFAULT_SYMBOLS

    plugin_raw = load_env_json("BINANCE_PLUGIN_MARKET_OVERVIEW_JSON")
    plugin_overview = normalize_plugin_overview(plugin_raw)
    fear_greed = plugin_overview.get("fear_greed") if plugin_overview.get("available") else {}
    if not fear_greed or fear_greed.get("value") is None:
        fear_greed = fetch_fear_greed()
    tickers = fetch_binance_tickers(symbols)
    binance_public_api_ok = any("error" not in item for item in tickers)
    coingecko_public_api_ok = False
    if not binance_public_api_ok:
        coingecko_tickers = fetch_coingecko_tickers()
        coingecko_public_api_ok = any("error" not in item for item in coingecko_tickers)
        if coingecko_public_api_ok:
            tickers = coingecko_tickers
    market = classify_market(fear_greed, tickers)
    keyword_signals = build_keyword_signals(plugin_overview, tickers, market, fear_greed)
    has_signal_notes = any(signal.get("market_signal_notes") for signal in keyword_signals.values())
    status = "ok" if binance_public_api_ok or coingecko_public_api_ok or plugin_overview.get("available") or has_signal_notes else "degraded"

    payload = {
        "generated_at": now_iso(),
        "status": status,
        "providers": {
            "binance_plugin": bool(plugin_overview.get("available")),
            "binance_public_api": binance_public_api_ok,
            "coingecko_public_api": coingecko_public_api_ok,
            "alternative_fear_greed": fear_greed.get("source") == "alternative.me",
        },
        "market": market,
        "fear_greed": fear_greed,
        "tickers": tickers,
        "plugin_overview": plugin_overview,
        "keyword_signals": keyword_signals,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    OUTPUT_MD.write_text(render_md(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
