import asyncio

import click
import jinja2

from pqapi import async_agent_query, async_query

bibtex = {}
references = []


async def pqa_filter(query, bibliography=None):
    response = await async_agent_query(query, bibliography=bibliography)
    global bibtex, references
    bibtex.update(response.bibtex)
    references.append(response.answer.references)
    return response.answer.answer


async def pqa_fast_filter(query, bibliography=None):
    response = await async_query(query, bibliography=bibliography)
    global bibtex, references
    bibtex.update(response.bibtex)
    references.append(response.answer.references)
    return response.answer.answer


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def main(filename):
    """This render the given template with calls to pqa"""
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("./"), enable_async=True)
    env.filters["pqa"] = pqa_filter
    env.filters["pqa_fast"] = pqa_fast_filter
    template = env.get_template(filename)

    # run it async
    loop = asyncio.get_event_loop()
    rendered_template = loop.run_until_complete(template.render_async())
    loop.close()

    # render template
    print(rendered_template + "\n\n")

    index = 0
    for refs in references:
        for ref in refs.split("\n\n"):
            if len(ref) < 5:
                continue
            index += 1
            # strip existing integer from reference
            ref = ref[ref.find(".") + 1 :]
            print(f"{index}.{ref}")
            print("\n")


if __name__ == "__main__":
    main()
