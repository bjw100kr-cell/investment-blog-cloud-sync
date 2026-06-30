#!/usr/bin/env python3
import json
import re
from pathlib import Path
from typing import Iterable, Optional


ROOT = Path(__file__).resolve().parents[1]
PIPELINE_SH = ROOT / "scripts/run_pipeline.sh"
WORKFLOW_YML = ROOT / ".github/workflows/daily-investment-intake.yml"
OUTPUT_JSON = ROOT / "outputs/latest/pipeline-workflow-parity.json"
OUTPUT_MD = ROOT / "outputs/latest/pipeline-workflow-parity.md"

PIPELINE_PATTERNS: tuple[re.Pattern[str], ...] = (
    # run_step calls: run_step "1/30" "Collect sources" python3 scripts/...
    re.compile(r"run_step\s+\"[^\"]+\"\s+\"[^\"]+\"\s+python3\s+(scripts/\S+\.py)"),
    # direct command line: python3 scripts/...
    re.compile(r"^\s*python3\s+(scripts/\S+\.py)"),
    # inline python expression from run_step helpers
    re.compile(r"\$\(dirname\s+\$0\)"),
)
WORKFLOW_STEP_RUN = re.compile(r"^\s*run:\s+(?:python|python3)\s+(scripts/\S+\.py)\s*$")
WORKFLOW_BLOCK_RUN_START = re.compile(r"^(\s*)run:\s*\|\s*$")
WORKFLOW_BLOCK_RUN_LINE = re.compile(r"^\s*(?:python3)\s+(scripts/\S+\.py)")
NON_PARITY_PIPELINE_SCRIPTS = {"scripts/emit_context_checkpoint.py", "scripts/persist_session_context.py"}


def _dedupe_consecutive(items: list[str]) -> list[str]:
    if not items:
        return []
    deduped = [items[0]]
    for item in items[1:]:
        if item != deduped[-1]:
            deduped.append(item)
    return deduped


def _match_script_name(patterns: Iterable[re.Pattern[str]], line: str) -> Optional[str]:
    for pattern in patterns:
        match = pattern.search(line)
        if match:
            script = match.group(1)
            # Guard against capturing incomplete tokens.
            if not script:
                continue
            return script.strip()
    return None


def parse_pipeline_scripts() -> list[str]:
    scripts: list[str] = []
    started = False
    for line in PIPELINE_SH.read_text().splitlines():
        if not started:
            if line.startswith("trap 'on_failure"):
                started = True
            continue

        script = _match_script_name(PIPELINE_PATTERNS, line)
        if script:
            if script in NON_PARITY_PIPELINE_SCRIPTS:
                continue
            scripts.append(script)
    return _dedupe_consecutive(scripts)


def parse_workflow_scripts() -> list[str]:
    scripts = []
    in_run_block = False
    run_block_indent = 0

    for line in WORKFLOW_YML.read_text().splitlines():
        if in_run_block:
            if not line.strip():
                continue
            indent = len(line) - len(line.lstrip())
            if indent <= run_block_indent:
                in_run_block = False
            else:
                direct_match = WORKFLOW_BLOCK_RUN_LINE.match(line)
                if direct_match:
                    scripts.append(direct_match.group(1))
                continue

        if not in_run_block:
            step_run_match = WORKFLOW_STEP_RUN.match(line)
            if step_run_match:
                scripts.append(step_run_match.group(1))
                continue

            block_match = WORKFLOW_BLOCK_RUN_START.match(line)
            if block_match:
                in_run_block = True
                run_block_indent = len(block_match.group(1))
    return scripts


def build_report() -> dict:
    pipeline_scripts = parse_pipeline_scripts()
    workflow_scripts = parse_workflow_scripts()

    missing_in_workflow = [script for script in pipeline_scripts if script not in workflow_scripts]
    missing_in_pipeline = [script for script in workflow_scripts if script not in pipeline_scripts]

    shared = [script for script in pipeline_scripts if script in workflow_scripts]
    order_mismatches = []
    for index, script in enumerate(shared):
        workflow_index = workflow_scripts.index(script)
        shared_index_in_workflow = sum(1 for item in workflow_scripts[:workflow_index] if item in shared)
        if shared_index_in_workflow != index:
            order_mismatches.append(
                {
                    "script": script,
                    "pipeline_shared_index": index,
                    "workflow_shared_index": shared_index_in_workflow,
                }
            )
    return {
        "pipeline_script_count": len(pipeline_scripts),
        "workflow_script_count": len(workflow_scripts),
        "missing_in_workflow": missing_in_workflow,
        "missing_in_pipeline": missing_in_pipeline,
        "order_mismatches": order_mismatches,
        "all_core_scripts_present": not missing_in_workflow and not missing_in_pipeline,
        "order_aligned": not order_mismatches,
        "pipeline_scripts": pipeline_scripts,
        "workflow_scripts": workflow_scripts,
    }


def write_markdown(report: dict) -> None:
    lines = []
    lines.append("# Pipeline Workflow Parity")
    lines.append("")
    lines.append("로컬 `run_pipeline.sh`와 GitHub Actions workflow 단계 정합성을 확인하는 리포트입니다.")
    lines.append("")
    lines.append(f"- pipeline_script_count: `{report.get('pipeline_script_count', 0)}`")
    lines.append(f"- workflow_script_count: `{report.get('workflow_script_count', 0)}`")
    lines.append(f"- all_core_scripts_present: `{report.get('all_core_scripts_present', False)}`")
    lines.append(f"- order_aligned: `{report.get('order_aligned', False)}`")
    lines.append("")
    lines.append("## Missing In Workflow")
    lines.append("")
    if report.get("missing_in_workflow"):
        for script in report.get("missing_in_workflow", []):
            lines.append(f"- `{script}`")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Missing In Pipeline")
    lines.append("")
    if report.get("missing_in_pipeline"):
        for script in report.get("missing_in_pipeline", []):
            lines.append(f"- `{script}`")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Order Mismatches")
    lines.append("")
    if report.get("order_mismatches"):
        for item in report.get("order_mismatches", []):
            lines.append(
                f"- `{item.get('script', '')}` / pipeline_shared_index `{item.get('pipeline_shared_index')}` / workflow_shared_index `{item.get('workflow_shared_index')}`"
            )
    else:
        lines.append("- none")
    OUTPUT_MD.write_text("\n".join(lines).strip() + "\n")


def main() -> int:
    report = build_report()
    OUTPUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    write_markdown(report)
    print(OUTPUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
