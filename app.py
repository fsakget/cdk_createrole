#!/usr/bin/env python3

from aws_cdk import core

from createrole.createrole_stack import CreateroleStack


app = core.App()
CreateroleStack(app, "createrole")

app.synth()
