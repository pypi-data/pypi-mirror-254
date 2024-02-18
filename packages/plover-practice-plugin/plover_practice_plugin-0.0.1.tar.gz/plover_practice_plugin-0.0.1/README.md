# Plover Practice Plugin

This [Plover][] [plugin][] project contains examples of the following types of
plugins:

- [Command][] (e.g. `"{:COMMAND:OPEN_URL:https://www.openstenoproject.org/}"`)
- [Meta][] (e.g. `"{:RANDOM_NUMBER:1:100}"`)
- [Extension][] (e.g. `"{:GET_ENV_VAR:$USER}"`)

It is a companion repo to the following blog post:

- _[Creating Plover Plugins with Python][]_

This plugin is meant for educational purposes only, and hence deliberately not
entered into the [Plover Plugins Registry][], so it will not show up in Plover's
Plugins Manager (though it has be released to [PyPI][], where you can find it
[here][PyPI plover-practice-plugin]).

## Install

I recommend following the blog post to build out the plugin yourself, but if you
just want to test it out on your machine, you can install it using [Git][]:

```sh
git clone git@github.com:paulfioravanti/plover-practice-plugin.git
cd plover-practice-plugin
plover --script plover_plugins install --editable .
```

> Where `plover` in the command is a reference to your locally installed version
> of Plover. See the [Invoke Plover from the command line][] page for details on
> how to create that reference.

### Enabling the Extension

- After re-opening Plover, open the Configuration screen (either click the
  Configuration icon, or from the main Plover application menu, select
  `Preferences...`)
- Open the Plugins tab
- Check the box next to `plover_practice_plugin` to activate
  the plugin

[Command]: https://plover.readthedocs.io/en/latest/plugin-dev/commands.html
[Creating Plover Plugins with Python]: https://www.paulfioravanti.com/blog/creating-plover-plugins-python/
[Extension]: https://plover.readthedocs.io/en/latest/plugin-dev/extensions.html
[Git]: https://git-scm.com/
[Invoke Plover from the command line]: https://github.com/openstenoproject/plover/wiki/Invoke-Plover-from-the-command-line
[Meta]: https://plover.readthedocs.io/en/latest/plugin-dev/metas.html
[PyPI]: https://pypi.org/
[PyPI plover-practice-plugin]: https://pypi.org/project/plover-practice-plugin/
[Plover]: https://www.openstenoproject.org/
[Plover Plugins Registry]: https://github.com/openstenoproject/plover_plugins_registry
[plugin]: https://plover.readthedocs.io/en/latest/plugins.html#types-of-plugins
