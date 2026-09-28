# OpenAI API examples with MuAPI

Use MuAPI's unified API to generate GPT Image images, create Sora videos, and run GPT reasoning models. This repository documents the OpenAI model families currently exposed by MuAPI and provides runnable cURL and Python examples.

[OpenAI API page on MuAPI](https://muapi.ai/openai-api) · [MuAPI](https://muapi.ai) · [API reference](https://muapi.ai/docs/api-reference) · [Get an API key](https://muapi.ai/access-keys)

## Related Projects

- [GPT Image API](https://github.com/Anil-matcha/GPT-Image-3-API) — image generation and editing examples.
- [Open Generative AI](https://github.com/Anil-matcha/Open-Generative-AI) — generative media tools and workflows.
- [AI Video API](https://github.com/Anil-matcha/AI-Video-API) — video model API examples.

## Coverage

The live MuAPI OpenAI catalog includes these distinct workflows:

| Family | Example endpoint | Inputs and use |
|---|---|---|
| GPT Image | `gpt-image-2-text-to-image`, `gpt-image-2-image-to-image`; GPT Image 2.5 Flare and Sunburst variants are also listed | Prompt-led image generation and image editing; image routes expose aspect ratio and resolution controls. |
| Sora | `openai-sora-2-text-to-video`, `openai-sora-2-image-to-video`, plus Pro routes | Text-to-video and image-to-video; Pro includes up to 1080p according to the MuAPI model catalog. |
| GPT reasoning | `gpt-6-astra` and other GPT reasoning endpoints | Text reasoning with configurable `reasoning_effort`; Astra accepts text and image input according to its catalog entry. |

This repository covers MuAPI's listed endpoints, not every OpenAI product or every parameter supported by OpenAI's own APIs. Check the live [OpenAI API page](https://muapi.ai/openai-api) and model playground pages for current availability and accepted fields.

## Choosing an endpoint

Compare endpoints against your workload rather than model names alone:

- **Task:** image generation, image editing, text-to-video, image-to-video, or text reasoning.
- **Input shape:** prompt only, source image URL, or text plus image input.
- **Controls:** aspect ratio, resolution, duration, and reasoning effort where the endpoint schema supports them.
- **Output and latency:** inspect the returned task status and output type; generation is asynchronous.
- **Cost:** compare the current MuAPI model page for the exact endpoint and settings. Pricing can vary by variant and output configuration; this README does not freeze rates.

## Quick start

Create a MuAPI key at [muapi.ai/access-keys](https://muapi.ai/access-keys), then set it in your shell:

```bash
export MUAPI_API_KEY="your_api_key"
```

Generation endpoints return a `request_id`. Poll `/api/v1/predictions/{request_id}/result` until the task completes and inspect its outputs. See `examples/submit.py` for an executable Python version.

## cURL examples

GPT Image generation:

```bash
curl -X POST "https://api.muapi.ai/api/v1/gpt-image-2-text-to-image" \
  -H "x-api-key: ${MUAPI_API_KEY}" -H "Content-Type: application/json" \
  -d '{"prompt":"Editorial product photo of a ceramic coffee cup on a warm wood table","aspect_ratio":"1:1","resolution":"2K"}'
```

Sora 2 Pro text-to-video:

```bash
curl -X POST "https://api.muapi.ai/api/v1/openai-sora-2-pro-text-to-video" \
  -H "x-api-key: ${MUAPI_API_KEY}" -H "Content-Type: application/json" \
  -d '{"prompt":"A slow tracking shot through a sunlit greenhouse","aspect_ratio":"16:9","duration":8,"resolution":"1080p"}'
```

GPT reasoning:

```bash
curl -X POST "https://api.muapi.ai/api/v1/gpt-6-astra" \
  -H "x-api-key: ${MUAPI_API_KEY}" -H "Content-Type: application/json" \
  -d '{"prompt":"Compare two database migration strategies and explain the tradeoffs.","reasoning_effort":"medium"}'
```

## Python example

Requires Python 3.9+ and `requests` (`python -m pip install requests`). Submit a selected example, then poll until it finishes:

```bash
python examples/submit.py image
python examples/submit.py sora
python examples/submit.py reasoning
```

The examples use the fields shown in MuAPI's OpenAI landing page snippets. For image-to-video, image editing, or other model variants, consult the live endpoint schema before changing the payload.

## Links

- [OpenAI API models and examples](https://muapi.ai/openai-api)
- [API reference](https://muapi.ai/docs/api-reference)
- [Playground: GPT Image](https://muapi.ai/playground/gpt-image-2-text-to-image)
- [Playground: Sora 2 Pro](https://muapi.ai/playground/openai-sora-2-pro-text-to-video)
- [Playground: GPT 6 Astra](https://muapi.ai/playground/gpt-6-astra)
- [Create or manage API keys](https://muapi.ai/access-keys)
