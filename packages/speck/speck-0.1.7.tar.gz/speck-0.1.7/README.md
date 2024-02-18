<p align="center">
    <img src="https://raw.githubusercontent.com/speckai/speck/main/assets/speck_banner.jpg">
</p>
<p align="center">
    <a href="https://pypi.org/project/speck/">
        <img src="https://img.shields.io/pypi/dm/speck" />
    </a>
    <a href="https://discord.gg/speck">
        <img src="https://dcbadge.vercel.app/api/server/frnaYYaKj3?style=flat" />
    </a>
    <a href="https://github.com/speckai/speck">
        <img src="https://img.shields.io/github/commit-activity/m/speckai/speck" />
    </a>
    <a href="https://linkedin.com/company/speck">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white" />
    </a>
</p>

---

<b>Speck</b> is a livetrace debugging and metrics tracking platform for LLM apps.

Speck streamlines LLM app development with its live debugging and metrics tracking. It simplifies prompt engineering and testing across any LLM, saving you time and enhancing your workflow.

### Features

Speck's main features include:

1. [Live LLM debugging]
2. [LLM observability](https://getspeck.ai/dash/home)
3. Developer framework for calling models
4. [OpenAI proxy](https://docs.getspeck.ai/development/openai)

### Support

| Model                                         | Support |
| --------------------------------------------- | :-----: |
| OpenAI                                        |   ✅    |
| AzureOpenAI                                   |   ✅    |
| Anthropic                                     |   ✅    |
| Replicate                                     |   ✅    |
| [LiteLLM](https://github.com/BerriAI/litellm) |   ✅    |

---

The [dashboard](https://getspeck.ai/dash/home) on the Speck website has 4 main features:

- Home: Dashboard for LLM usage metrics
- Logs: Inspect recent LLM calls
- Playground: Prompt engineer with any model
- Live Debug: Test prompts with on-the-fly debugging

If you have any feature requests or want to stay up to date, please join our [Discord community](https://discord.gg/speck)!

---

## Getting Started

### Python

```shell
pip install speck
```

Then, you can run something like:

```python
from speck import Speck
client = Speck(api_key=None, api_keys={"openai": "sk-...", "anthropic": "sk-..."})
response: Response = client.chat.create(
    prompt=[{"role": "system", "content": "Count to 5."}],
    config={"model": "anthropic:claude-2"}
)
```

Now, each call will be logged for testing. Read more on our [documentation](https://docs.getspeck.ai)!
