# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
"""
Azure AI Vision SDK -- Python Image Analysis Samples

Main entry point for the sample application.
"""

import sys
import platform
import secrets
import samples


def print_usage():
    print()
    print(' To run the samples:')
    print()
    print('   python main.py [--key|-k <your-key>] [--endpoint|-e <your-endpoint>]')
    print()
    print(' Where:')
    print('   <your-key> - A computer vision key you get from your Azure portal.')
    print('     It should be a 32-character HEX number.')
    print('   <your-endpoint> - A computer vision endpoint you get from your Azure portal.')
    print('     It should have the form:')
    print('     https://<your-computer-vision-resource-name>.cognitiveservices.azure.com')
    print()
    print(' As an alternative to specifying the above command line arguments, you can specify')
    print(' these environment variables: {} and/or {}.'.format(secrets.ENVIRONMENT_VARIABLE_KEY,
                                                               secrets.ENVIRONMENT_VARIABLE_ENDPOINT))
    print()
    print(' To get this usage help, run:')
    print()
    print('   python main.py --help|-h')
    print()


def select():
    abort_key = 'Ctrl-Z' if "Windows" == platform.system() else 'Ctrl-D'

    sample_functions = [
        samples.get_all_results,
        samples.get_results_using_analyzed_event,
    ]

    print(' Select sample or {} to abort:'.format(abort_key))
    print()
    for i, fun in enumerate(sample_functions):
        print(" {}: {}\n{}".format(i, fun.__name__, fun.__doc__))

    try:
        num = int(input())
        selected_function = sample_functions[num]
    except EOFError:
        raise
    except Exception as e:
        print(e)
        return

    print('You selected: {}'.format(selected_function))
    try:
        selected_function()
    except Exception as e:
        print('Error running sample: {}'.format(e))

    print()


print()
print(' Azure AI Vision SDK - Image Analysis Samples')
print()

for arg in sys.argv:
    if arg in ['--help', '-h']:
        print_usage()
        sys.exit(0)

if not secrets.load_succeeded(sys.argv):
    print_usage()
    sys.exit(1)

while True:
    try:
        select()
    except EOFError:
        break
