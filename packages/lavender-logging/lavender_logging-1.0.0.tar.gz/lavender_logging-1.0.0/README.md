# Lavender Logging

Lavender Logging is a logger configuration system designed to simplify the process of configuring your logger to only log the messages you want to see.

## Usage

To use Lavender simply call `lavender.setup()` instead of `logging.basicConfig()`. This will enable all of Lavender's features and ensure it works as intended.

Lavender uses its own filter system, configured using patterns which match package names. For example `discord.*` matches all submodules of the `discord` package. Filters can be added using the `filter_config` parameter of `lavender.setup` or using environment variables.

Lavender looks for evironment variables with `LOG_DEBUG`, `LOG_INFO`, `LOG_WARNING` etc to extract patterns from. Multiple patterns can be specified for the same log level by separating them with `os.pathsep`. For example, the following will set the log level of `amethyst.client` and all submodules of `discord` and to `ERROR` on windows.

```
LOG_ERROR="amethyst.client;discord.*"
```

Filters that infer more of a package's path with wildcards have less priority over more specific patterns. For example with the patterns `discord.*` and `discord.gateway.*`, `discord.gateway.*` will have priority.
