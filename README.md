# DeepUserModelling
> Deep learnt user model for scientific paper recommendation

> First of all, we converted the raw dataset into one which contains all the datas inside the tags. This ensured that we can easily identify the data. Next we extracted the unique authors and their papers which were identified with thier identifiers. Thus we got all the authors having unique papers.
>
> Now, we made an adjacency list of the authors by using the citation informations provided. We then made a look-up table so as to make a citation network graph. Now from the graph we determined diiffernt communities and also the major communities that had substantial population. The papers that were not involved in any community, had to be included in the nearest community.
>
> We also retrained the **Skip Thoughts** because we didn't get the desired efficiency. We had to train it on our dataset. Also we made the vector representation of our dataset using word2vec.

> Given below are some of the important codes that we used to _process_ our data.

## new_dataset_gen.py
* **Input**: The initial text file containing the information about papers.
* **Output**: All the data placed under _tags_.
* **Relevance**: We converted the data into this format so that it could be identified easily.

## dataprep.py
* **Input**: Dataset of papers
* **Output**: Identifiers for all the papers
* **Relevance**: We generated the identifiers for the papers so as to access the papers.

## citation_network_gen.py
* **Input**: Dataset of papers
* **Output**: Adjacency List
* **Relevance**: To make the _Network Graph_ for different categories of the authors.

## author_papers_gen.py
* **Input**: Dataset of papers
* **Output**: List of authors and their paper identifiers
* **Relevance**: We made a list of authors and their papers (paper identifiers).

## histogram_plotter.py
* **Input**: Count of papers for different authors
* **Output**: Histogram for the papers
* **Relevance**: This gives us the desired range of authors to be included in our final list.

## histogram_plot_for_look_up_table.py
* **Input**: Populations in each category determined from the adjacency list
* **Output**: Histogram plot showing _Population of Communities_ and their _Frequencies_
* **Relevance**: This gives us the major categories for our network.

## input_for_skip_thought_vectors.py
* **Input**: The entire dataset of papers
* **Output**: The dataset generated in desired format from the abstracts for the training of _Skip Thoughts_
* **Relevance**: We need to retrain the _Skip Thoughts_ so as to get the desired efficiency of the program.

## look_up_table.py
* **Input**: Adjacency List
* **Output**: A look up table for the indices
* **Relevance**: For the infomap generation we need the indices starting from 0 or 1. So we had to convert the indices of the papers and therefore we mapped the indices.

## paper_reader.py
* **Input**: Dataset of papers
* **Output**: A small dataset of papers
* **Relevance**: We made a small dataset of papers so as to do tests on them

## final_dataset_of_authors_with_their_paper_identifiers.py
* **Input**: Dataset of all the papers with their abstracts and the list of all the authors of interest
* **Output**: List of authors with their paper identifiers
 * **Relevance**: We made a list of authors and all the papers (paper identifiers) written by that author