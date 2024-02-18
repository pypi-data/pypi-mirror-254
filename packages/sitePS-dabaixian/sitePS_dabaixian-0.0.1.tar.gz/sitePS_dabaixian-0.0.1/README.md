Target: Input a human gene sequence and output the phylogenetic age of each amino acid position in the sequence.

eg:

`from sitePS_dabaixian import sitePS`

`sitePS(query_name, output_name, evalue, threads, add, delete)`

`query_name` and `output_name` are necessary, they are string types, that is, the name of the input query file and the name of the file to be output. `evlaue` and `threads` are also string types but are optional. They default to 1e-4 and 64 respectively. `add` represents adding species, which is a string type and is the name of a file. `delete` represents removing some species and is a list type. Similar to [22,23,25]

If you want to add species
You need to give a file, the content of the file is as follows
`1328070,20,Prolemur simus`
`379532,20,Propithecus coquereli`
`10029,19,Cricetulus griseus`
`10181,19,Heterocephalus glaber`

We automatically use blast to compare the species in our library with the query. Based on the comparison results, we query each layer layer by layer from 27 downwards to see whether the site is consistent with the human amino acid. If there is no amino acid position consistent with human beings in the n layer, no further progress will be made. The position will be located in the n+1 layer.