import click
import itertools
import sys
import yaml

def echo_yaml(data):
    """Echo data in YAML format."""
    yaml_data = yaml.dump(data, default_flow_style=False)
    click.echo(yaml_data)

def echo_yaml_tuples(iterable):
    data = [list(x) for x in iterable]
    echo_yaml(data)

def set_iterable(iterable):
    return iterable if iterable else [line.strip() for line in sys.stdin] 

def set_element(element):
    return element if element else str(sys.stdin)

# Helper function to limit the output of infinite iterators
def limited_list(iterator, limit):
    result = []
    for i, item in enumerate(iterator):
        if i >= limit:
            break
        result.append(item)
    return result

@click.group()
def cli():
    """CLI tool for demonstrating Python's itertools functions."""
    pass

@click.command()
@click.argument('start', type=int)
@click.argument('step', type=int)
@click.option('--limit', default=10, help='Limit the number of items to generate')
def count(start, step, limit):
    """Generate an infinite sequence of evenly spaced values."""
    result = limited_list(itertools.count(start, step), limit)
    echo_yaml(result)

@click.command()
@click.argument('sequence', nargs=-1)
@click.option('--limit', default=10, help='Limit the number of items to cycle through')
def cycle(sequence, limit):
    """Cycle through a sequence indefinitely."""
    sequence = set_iterable(sequence)
    result = limited_list(itertools.cycle(sequence), limit)
    echo_yaml(result)

@click.command()
@click.argument('element')
@click.option('--times', default=5, help='Number of repetitions')
def repeat(element, times):
    """Repeat an element for a specified number of times."""
    element = set_element(element)
    result = list(itertools.repeat(element, times))
    echo_yaml(result)

@click.command()
@click.argument('elements', nargs=-1)
@click.argument('r', type=int)
def combinations(elements, r):
    """Generate all possible combinations of a given length."""
    elements = set_iterable(elements)
    echo_yaml_tuples(itertools.combinations(elements, r))

@click.command()
@click.argument('elements', nargs=-1)
@click.argument('r', type=int)
def combinations_with_replacement(elements, r):
    """Generate all possible combinations of a given length."""
    elements = set_iterable(elements)
    echo_yaml_tuples(itertools.combinations_with_replacement(elements, r))

@click.command()
@click.argument('elements', nargs=-1)
@click.argument('r', type=int)
def permutations(elements, r):
    """Generate all possible permutations of a given length."""
    elements = set_iterable(elements)
    echo_yaml_tuples(itertools.permutations(elements, r))

@click.command()
@click.argument('elements', nargs=-1)
@click.option('--repeat', default=1, type=int, help='Number of repetitions')
def product(elements, repeat):
    """Generate the cartesian product of elements iterables."""
    elements = set_iterable(elements)
    echo_yaml_tuples(itertools.product(elements, repeat=repeat))

@click.command()
@click.argument('elements', nargs=-1)
def chain(elements):
    """Chain multiple iterables into a single one."""
    elements = set_iterable(elements)
    result = list(itertools.chain(elements))
    echo_yaml(result)

@click.command()
@click.argument('iterable', nargs=-1)
@click.option('--start', default=0, type=int, help='Starting index')
@click.option('--stop', default=None, type=int, help='Ending index')
@click.option('--step', default=1, type=int, help='Step')
def islice(iterable, start, stop, step):
    """Slice an iterable from start to stop with a step."""
    sliced = itertools.islice(iterable, start, stop, step)
    result = list(sliced)
    echo_yaml(result)

@click.command()
@click.argument('data', nargs=-1)
@click.argument('selectors_str')
def compress(data, selectors_str):
    """Filter one iterable with another."""
    selectors = [int(x) for x in selectors_str]
    result = list(itertools.compress(data, selectors))
    echo_yaml(result)


@click.command()
@click.argument('iterable', nargs=-1)
def pairwise(iterable):
    """Return pairs of consecutive elements."""
    echo_yaml_tuples(itertools.pairwise(iterable))

cli.add_command(count)
cli.add_command(cycle)
cli.add_command(repeat)
cli.add_command(combinations)
cli.add_command(combinations_with_replacement)
cli.add_command(permutations)
cli.add_command(product)
cli.add_command(chain)
cli.add_command(islice)
cli.add_command(compress)
cli.add_command(pairwise)

if __name__ == '__main__':
    cli()
