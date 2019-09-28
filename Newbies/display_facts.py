#!/usr/bin/env python3
"""Display facts."""


def display_facts(facts):
    """Display facts."""
    for fact in facts:
        print('{}: {}'.format(fact, facts[fact]))
        print()


FACTS = {
    'David': 'Was a mascot in college.',
    'Jeff': 'Was born in France.',
    'Anna': 'Has arachnophobia.'
}

display_facts(FACTS)

FACTS['David'] = 'Can juggle.'
FACTS['Dylan'] = 'Has a pet hedgehog.'

display_facts(FACTS)
