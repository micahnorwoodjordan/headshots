# objective

- to deploy a generative ai diffusion pipeline for the purpose of creating professional headshots. a user should be able to upload a simple `jpeg` / `png` and get back an AI-generated headshot

## determining an appropriate model

`huggingface.co` allows you to test different models on inference provider(s) of your choice conveniently within the browser. as of now, the forked qwen model `dx8152/Qwen-Edit-2509-Multiple-angles` seems to be the most accurate.

- selected model: <https://huggingface.co/dx8152/Qwen-Edit-2509-Multiple-angles?inference_provider=wavespeed>


---

## definitions

- ***ACCURATE***: *m / n inference operations meet expectations*
- ***FAST***: < 15s inference
- ***CHEAP***: < $20 / month


## requirements

### models and infrastructure / hosting

- [***ACCURATE***](#definitions)
- [***FAST***](#definitions)
- [***CHEAP***](#definitions) inference / generation

---
