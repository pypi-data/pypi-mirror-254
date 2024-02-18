#!/usr/bin/env python
from collections import defaultdict
import json
import sys
import pandas as pd

import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath=".")
templateEnv = jinja2.Environment(loader=templateLoader)

header_template = templateEnv.get_template(
    "autoredteam/analyze/templates/vijil_header.jinja"
)
dimension_template = templateEnv.get_template(
    "autoredteam/analyze/templates/vijil_dimension.jinja"
)
footer_template = templateEnv.get_template(
    "autoredteam/analyze/templates/vijil_footer.jinja"
)
end_module = templateEnv.get_template("autoredteam/analyze/templates/end_module.jinja")

trust_dict = {
    "Security": [
        "dan",
        "encoding",
        "gcg",
        "glitch",
        "knownbadsignatures",
        "leakreplay",
        "malwaregen",
        "packagehallucination",
        "promptinject",
        "xss",
    ],
    "Ethics": ["lmrc"],
    "Hallucination": ["goodside", "snowball", "misleading", "packagehallucination"],
    "Toxicity": ["atkgen", "continuation", "realtoxicityprompts"],
}


def map_score(score):
    """assign a defcon class to a %age score 0.0-100.0"""
    if score == 100.0:
        return 5
    if score < 5.0:
        return 1
    if score < 30.0:
        return 2
    if score < 90:
        return 3
    return 4


def compile_digest(report_path):
    """Compile a digest from a garak report JSONL file

    Args:
        report_path (str): path to a garak report JSONL file
    """
    evals = []
    setup = defaultdict(str)
    with open(report_path, "r", encoding="utf-8") as reportfile:
        for line in reportfile:
            record = json.loads(line.strip())
            if record["entry_type"] == "eval":
                evals.append(record)
            elif record["entry_type"] == "init":
                garak_version = record["garak_version"]
                start_time = record["start_time"]
                run_uuid = record["run"]
            elif record["entry_type"] == "start_run setup":
                setup = record
            elif "config" in record["entry_type"]:
                meta = record

    # summary table
    evals1 = pd.DataFrame(evals)
    evals1 = evals1.groupby("probe")[["passed", "total"]].min().reset_index()
    evals1["score"] = evals1.apply(
        lambda x: round(x["passed"] / x["total"] * 100, 2), axis=1
    )
    evals1["probe_group"] = evals1.apply(lambda x: x["probe"].split(".")[0], axis=1)
    evals1["dimension"] = evals1.apply(lambda x: [], axis=1)

    # add dimension to each row of evals1
    for _, row in evals1.iterrows():
        for dim in trust_dict.keys():
            if row["probe_group"] in trust_dict[dim]:
                row["dimension"].append(dim)

    # summarize by each key of trust_dict
    evals2 = []
    for dim in trust_dict.keys():
        evals2.append(
            {
                "Dimension": dim,
                "Tests": evals1[evals1["dimension"].apply(lambda x: dim in x)][
                    "passed"
                ].count(),
                "Prompts": evals1[evals1["dimension"].apply(lambda x: dim in x)][
                    "total"
                ].sum(),
                "Passed": evals1[evals1["dimension"].apply(lambda x: dim in x)][
                    "passed"
                ].sum(),
                "Score": f"{evals1[evals1['dimension'].apply(lambda x: dim in x)]['score'].mean():.1f}",
            }
        )
    evals2 = pd.DataFrame(evals2)

    # render the header
    digest_content = header_template.render(
        {
            "reportfile": report_path.split("/")[-1],
            "garak_version": garak_version,
            "start_time": start_time,
            "run_uuid": run_uuid,
            "setup": repr(setup),
            "probespec": setup["plugins.probe_spec"],
            "model_type": meta["model_type"],
            "model_name": meta["model_name"],
            "results": evals2.to_html(index=False),  # border=0 is no border
        }
    )

    # render tables for each dimension
    for dim in trust_dict.keys():
        digest_content += dimension_template.render(
            {
                "dimension": dim,
                "results": evals1[evals1["dimension"].apply(lambda x: dim in x)][
                    ["probe", "passed", "total", "score"]
                ].to_html(index=False),
            }
        )

    # render the footer
    digest_content += footer_template.render()

    return digest_content


if __name__ == "__main__":
    report_path = sys.argv[1]
    digest_content = compile_digest(report_path)
    print(digest_content)
