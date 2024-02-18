#!/usr/bin/env python3
from resemble.protoc_gen_resemble_generic import (
    PluginSpecificData,
    ResembleProtocPlugin,
)


class PythonResembleProtocPlugin(ResembleProtocPlugin):

    @staticmethod
    def plugin_specific_data() -> PluginSpecificData:
        return PluginSpecificData(
            template_filename="resemble.py.j2",
            output_filename_suffix="_rsm.py",
            supported_features=[
                "reader", "writer", "transaction", "task", "error", "streaming"
            ]
        )


# This is a separate function (rather than just being in `__main__`) so that we
# can refer to it as a `script` in our `pip_package` BUILD targets.
def main():
    PythonResembleProtocPlugin.execute()


if __name__ == '__main__':
    main()
