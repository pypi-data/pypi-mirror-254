# autoredteam

Automated Red Teaming Test suite by [vijil](https://www.vijil.ai/).

## CLI calling patterns

```
python -m autoredteam --model_type <> --model_name <> --tests <>
```

For a model provider, there are three possible deployment types: local model, public API, and private endpoint. Some providers offer only a subset of these deployment types.

The following table provides respective `--model_type` values for each such provider x deployment type. If a deployment type is not listed for a provider, the respective radio button should be inactive in the GUI.

| Agent | Deployment Type | `model_type`
|---|---|---|
| Anyscale | public API | `anyscale` |
| Hugging Face | local model | `huggingface` |
| | public API | `huggingface.InferenceAPI` |
| | private endpoint | `huggingface.InferenceEndpoint` |
| Mistral | public API | `mistral` |
| Replicate | public API | `replicate` |
| | private endpoint | `replicate.ReplicateEndpoint` |
| OctoAI | public API | `octo` |
| | private endpoint | `octo.OctoEndpoint` |
| OpenAI | public API | `openai` |
| Together | public API | `together` |
