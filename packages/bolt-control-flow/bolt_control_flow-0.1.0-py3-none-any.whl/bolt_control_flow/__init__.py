__version__ = "0.1.0"


from beet import Context
from beet.contrib.load import load
from bolt import Runtime

from bolt_control_flow.helpers import get_runtime_helpers
from bolt_control_flow.parse import Codegen

# Make the contents of these modules available directly in `from bolt_control_flow import ...`
from bolt_control_flow.types import *


def beet_default(ctx: Context):
    ctx.require(
        load(
            data_pack={
                "data/bolt_control_flow/modules": "@bolt_control_flow/modules",
            },
        ),
    )

    runtime = ctx.inject(Runtime)
    runtime.helpers.update(get_runtime_helpers())
    runtime.modules.codegen.extend(Codegen())
