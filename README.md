# HC - hasCycle

Il presente file descrive brevemente il contenuto della repository e forinsce informazioni generali riguardanti il lavoro svolto.
La funzione ``hasCycle(G)`` controlla se in dato grafo G è presente almeno un ciclo. essa è stata implementata in due varianti, HCDFS e HCUF, descritte meglio nelle rispettive sezioni.
I grafi passati come input sono generati dalla funzione ``gGenerator(nodes, range, cycle=False)``. 
I dati prestazionali riguardanti l'esecuzione di HC sono registrati dal decoratore ``@profiler``.
Maggiori informazioni sono reperibili nella cartella ``Relazione``.

**GG_module.py**

Modulo contenente la definizione di ``gGenerator()``, che si occupa di generare grafi non orientati connessi aciclici, a cui saranno aggiunti ``cycle`` cicli al grafo.

**HCDFS_module.py**

Modulo contenente una variante di implementazione di HC, che sfrutta la visita DFS e dei contatori per individuare la presenza di un ciclo.

**HCUF_module.py**

Modulo contenente una variante di implementazione di HC, che sfrutta la struttura dati Union-Find per verificare la presenza di un ciclo, accedendo ai nodi dei set con il metodo ``findNode(e)`` e scorrendo gli archi con l'ausilio del generatore ``edgeGenerator(G, maxTail, maxHead)``.

**D_module.py**

In tale modulo è descritto il decoratore ``@profiler``, che annota i dati prestazionali della funzione su cui è applicato in un file di testo a scelta dell'utente, di default ``log.txt``.

**Graph, unionfind**

Cartelle contenenti le strutture dati utilizzate per svolgere il lavoro.

**Pics**

Cartella contenente immagini, schemi e grafici realizzati per stendere la relazione. 

**Autori**

Jianu    Mihai    0255043
La Prova Daniele  0253508
Mei      Lorenzo  0251766
