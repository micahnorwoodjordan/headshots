# AI Headshot Generator

## Objective

Deploy a generative AI diffusion pipeline capable of creating professional headshots from user-provided images.

The intended workflow is:

1. User uploads a `JPEG` or `PNG`.
2. The image is passed through a generative image-editing pipeline.
3. The pipeline generates a professional headshot.
4. The generated headshot is returned to the user.

## Model Selection

[Hugging Face](https://huggingface.co/) provides a convenient way to evaluate different models through a variety of inference providers directly in the browser.

As of the current evaluation, the forked Qwen model `dx8152/Qwen-Edit-2509-Multiple-angles` has produced the most accurate results.

**Selected model:**
[dx8152/Qwen-Edit-2509-Multiple-angles](https://huggingface.co/dx8152/Qwen-Edit-2509-Multiple-angles?inference_provider=wavespeed)

## Definitions

| Term         | Definition                                     |
| ------------ | ---------------------------------------------- |
| **ACCURATE** | `m / n` inference operations meet expectations |
| **FAST**     | Inference completes in `< 15s`                 |
| **CHEAP**    | Infrastructure costs `< $20 / month`           |

## Requirements

### Model & Infrastructure

The inference solution should be:

* **[ACCURATE](#definitions)**
* **[FAST](#definitions)**
* **[CHEAP](#definitions)**

## Infrastructure Evaluation

### DigitalOcean GPU Droplets

[DigitalOcean GPU Droplets]()
