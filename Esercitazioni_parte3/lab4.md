## 📊 Tabella Comparativa delle Configurazioni

| Parametro / Metrica | Configurazione 1 | Configurazione 2 | Configurazione 3 |
| :--- | :---: | :---: | :---: |
| **UMAP: Componenti (`n_components`)** | 5 | 10 | 15 |
| **UMAP: Distanza Minima (`min_dist`)** | 0.0 | 0.1 | 0.1 |
| **UMAP: Metrica** | `cosine` | `cosine` | `euclidean` |
| **UMAP: Vicini (`n_neighbors`)** | *Default* | *Default* | 15 |
| **HDBSCAN: Dimensione Minima (`min_cluster_size`)** | 50 | 100 | 200 |
| **HDBSCAN: Selezione (`cluster_selection_method`)** | `eom` | `leaf` | `eom` |
| **HDBSCAN: metric** | `euclidean` | `euclidean` | `euclidean` |
| **Numero di Topic Emersi** | **158** | **81** | **32** |
| **Percentuale di Outliers (Rumore)** | **34.57%** | **53.34%** | **44.37%** |
| **Tempo computazionale** | **56.36s** | **78.67s** | **83.65s** |

---
## Parole Chiave (Top-5) per Configurazione

### Configurazione 1
* **Topic 0:** `speech`, `asr`, `recognition`, `end`, `acoustic`
* **Topic 1:** `medical`, `clinical`, `biomedical`, `patient`, `health`
* **Topic 2:** `translation`, `nmt`, `machine`, `bleu`, `neural`
* **Topic 3:** `hate`, `offensive`, `speech`, `detection`, `toxic`
* **Topic 4:** `relation`, `extraction`, `re`, `relations`, `entity`
* **Topic 5:** `gender`, `bias`, `biases`, `debiasing`, `fairness`
* **Topic 6:** `ner`, `entity`, `named`, `recognition`, `entities`
* **Topic 7:** `word`, `embeddings`, `embedding`, `similarity`, `vectors`
* **Topic 8:** `summarization`, `abstractive`, `summary`, `summaries`, `document`
* **Topic 9:** `agents`, `agent`, `game`, `games`, `environment`

### Configurazione 2
* **Topic 0:** `summarization`, `summaries`, `summary`, `abstractive`, `document`
* **Topic 1:** `hate`, `offensive`, `speech`, `detection`, `social`
* **Topic 2:** `relation`, `extraction`, `re`, `relations`, `entity`
* **Topic 3:** `translation`, `nmt`, `machine`, `neural`, `english`
* **Topic 4:** `gender`, `bias`, `biases`, `debiasing`, `in`
* **Topic 5:** `speech`, `asr`, `recognition`, `acoustic`, `end`
* **Topic 6:** `image`, `visual`, `multimodal`, `images`, `vision`
* **Topic 7:** `reasoning`, `cot`, `math`, `llms`, `mathematical`
* **Topic 8:** `arabic`, `morphological`, `pos`, `languages`, `tagging`
* **Topic 9:** `event`, `events`, `causal`, `temporal`, `extraction`

### Configurazione 3
* **Topic 0:** `dialogue`, `the`, `to`, `and`, `dialog`
* **Topic 1:** `sentiment`, `the`, `emotion`, `and`, `of`
* **Topic 2:** `speech`, `asr`, `the`, `recognition`, `to`
* **Topic 3:** `question`, `answer`, `questions`, `qa`, `answering`
* **Topic 4:** `translation`, `nmt`, `machine`, `the`, `to`
* **Topic 5:** `summarization`, `summaries`, `the`, `summary`, `of`
* **Topic 6:** `medical`, `clinical`, `and`, `the`, `of`
* **Topic 7:** `the`, `tuning`, `attention`, `to`, `transformer`
* **Topic 8:** `word`, `embeddings`, `of`, `the`, `embedding`
* **Topic 9:** `ner`, `entity`, `named`, `entities`, `the`

---
#### Topic estratti dalla configurazione 1

### Topic 0: Automatic Speech Recognition (ASR) & Acoustics
* **Parole chiave:** `speech`, `asr`, `recognition`, `end`, `acoustic`
* **Sintesi dei Documenti Rappresentativi:**
  * *Doc 1:* Tratta l'estensione dei sistemi di riconoscimento vocale automatico (ASR) integrando audio sintetico generato da modelli Text-to-Speech (TTS).
  * *Doc 2:* Discute l'importanza dell'informazione del contesto conversazionale a livello macro per migliorare i modelli di riconoscimento vocale end-to-end.
  * *Doc 3:* Analizza la scarsità di dati per il processamento del linguaggio vocale (speech tasks) e propone un approccio non supervisionato per la traduzione vocale (speech translation).
* **Valutazione della Coerenza:** **Eccellente.** Tutti e tre i documenti appartengono strettamente al dominio dell'audio/speech processing. I termini estratti riflettono perfettamente il nucleo tematico delle architetture tecniche esaminate.

### Topic 1: Clinical & Healthcare NLP
* **Parole chiave:** `medical`, `clinical`, `biomedical`, `patient`, `health`
* **Sintesi dei Documenti Rappresentativi:**
  * *Doc 1:* Analizza l'uso delle note cliniche non strutturate nel settore medico per l'estrazione automatica di attributi e cartelle cliniche elettroniche (EHR).
  * *Doc 2:* Tratta l'apprendimento di rappresentazioni distribuite (embeddings) di concetti medici a partire dalle cartelle cliniche per supportare le decisioni cliniche.
  * *Doc 3:* Esamina l'utilizzo dei record medici elettronici (EMR/EHR) e l'applicazione di modelli Transformer per convertire le annotazioni cliniche testuali.
* **Valutazione della Coerenza:** **Massima.** Il gruppo mostra una stabilità interna totale. Il focus non è genericamente "medico", ma è iperspecifico sull'applicazione del Text Mining e dei modelli linguistici sui dati clinici testuali delle cartelle sanitarie.

### Topic 2: Neural Machine Translation (NMT)
* **Parole chiave:** `translation`, `nmt`, `machine`, `bleu`, `neural`
* **Sintesi dei Documenti Rappresentativi:**
  * *Doc 1:* Introduce l'evoluzione della qualità della traduzione automatica sul web, focalizzandosi sul recente approccio della traduzione automatica neurale (NMT).
  * *Doc 2:* Investiga l'utilizzo di dati monolingua lato target per migliorare la fluidità e le prestazioni dei sistemi di Neural Machine Translation (NMT).
  * *Doc 3:* Affronta i limiti dei sistemi NMT nella traduzione di lingue a basse risorse (low-resourced) causati dalla scarsità di corpora paralleli.
* **Valutazione della Coerenza:** **Eccellente.** I confini del cluster sono netti e non presentano alcuna sovrapposizione con altri task. Tutti gli abstract mappano lo stato dell'arte e le problematiche della traduzione automatica.

### Topic 3: Hate Speech & Toxicity Detection
* **Parole chiave:** `hate`, `offensive`, `speech`, `detection`, `toxic`
* **Sintesi dei Documenti Rappresentativi:**
  * *Doc 1:* Discute l'identificazione automatica del linguaggio d'odio (hate speech) sui social media al fine di contrastare fenomeni di polarizzazione sociale e crimini d'odio.
  * *Doc 2:* Analizza i sistemi di classificazione di contenuti online negativi mirati a gruppi specifici, evidenziando la difficoltà di espandere questi modelli su più lingue.
  * *Doc 3:* Tratta la necessità urgente di contromisure e metodi computazionali per classificare automaticamente i testi dei social media in categorie "hate" o "non-hate".
* **Valutazione della Coerenza:** **Eccellente.** Il cluster dimostra una forte coerenza tematica di tipo applicativo/societario. La parola `speech` qui è usata nel contesto di "linguaggio" (hate speech) e non di "traccia audio", mostrando come il modello riesca a disambiguare i termini in base al contesto del cluster.

### Topic 4: Relation Extraction (RE)
* **Parole chiave:** `relation`, `extraction`, `re`, `relations`, `entity`
* **Sintesi dei Documenti Rappresentativi:**
  * *Doc 1:* Propone un modello basato su curriculum learning per la Relation Extraction (RE) a livello di singola frase, affrontando il problema dei dati rumorosi.
  * *Doc 2:* Discute l'importanza dell'estrazione delle relazioni tra entità nei testi per la costruzione di basi di conoscenza (Knowledge Base) e per la comprensione del testo.
  * *Doc 3:* Esamina i modelli di estrazione delle relazioni tramite supervisione a distanza (*distant supervised*) introducendo l'uso delle informazioni sintattiche per modellare le entità.
* **Valutazione della Coerenza:** **Massima.** Il cluster mappa in modo impeccabile un sub-task classico dell'Information Extraction. Tutti i documenti affrontano la stessa identica sfida geometrica e linguistica: legare due entità nominali tramite la loro relazione sintattica/semantica.

--- 
# Analisi Comparativa delle Configurazioni di Clustering (BERTopic)

## Analisi Critica: Quale configurazione produce topic più interpretabili?

Dall'analisi dettagliata dei dati e dei cluster estratti, la **Configurazione 1** produce i topic di gran lunga più interpretabili, definiti e semanticamente coerenti.

L'interpretabilità di un modello di Topic Modeling si valuta sulla *purezza semantica* delle parole chiave e sulla *coerenza interna* dei documenti rappresentativi. La Configurazione 1 risulta migliore per tre ragioni principali:
* **Disambiguazione contestuale perfetta:** Il modello è in grado di separare la parola `speech` intesa come segnale vocale/audio (allocata nel *Topic 0: ASR*) da `speech` intesa come espressione/testo sociale (allocata nel *Topic 3: Hate Speech*). Questo dimostra che lo spazio vettoriale ridotto ha conservato le relazioni semantiche più sottili.
* **Assenza di stopword generiche:** Le top-5 parole chiave contengono solo termini tecnici ad altissimo valore informativo (es. `asr`, `nmt`, `bleu`, `debiasing`, `ehr`).
* **Granularità ottimale:** Con 158 topic, il modello non si ferma alla superficie (es. "Medicina"), ma scende a un livello di specificità migliore (es. *Topic 1: Text Mining su cartelle cliniche elettroniche/EHR*).

Le configurazioni 2 e 3 mostrano un progressivo degrado della qualità.
* **Configurazione 2:** Tra le parole chiave iniziano a comparire termini strutturali non informativi come `in` (Topic 4). Inoltre, l'algoritmo inizia a fondere concetti diversi a causa dell'aumento di `min_cluster_size` (100).
* **Configurazione 3:** La quasi totalità dei topic è dominata da stopwords (`the`, `to`, `and`, `of`), rendendo i cluster indistinguibili e inutilizzabili.
  * *Perché è successo?* È un effetto geometrico. Avendo impostato la metrica di UMAP su `euclidean` (invece di `cosine`) e avendo alzato drasticamente le componenti e la dimensione minima dei cluster, HDBSCAN ha raggruppato i documenti non più in base al loro significato, ma in base alla loro struttura sintattica o lunghezza (documenti che usano gli stessi articoli/preposizioni sono finiti insieme).

---

| Scelta Algoritmica | Vantaggio | Svantaggio | Effetto Visibile nei Dati |
| :--- | :--- | :--- | :--- |
| **`n_components: 5` + `cosine`** | Conserva le relazioni semantiche strette negli embeddings di testo. | Rischio di perdere macro-informazioni globali. | **Configurazione 1:** Topic cristallini e iper-specifici. |
| **`min_cluster_size` Alto** | Meno topic da analizzare (maggiore capacità di sintesi). | I topic si fondono e diventano generici/vuoti. | **Configurazione 3:** Solo 32 topic, ma semanticamente distrutti. |
| **Selezione `leaf` (HDBSCAN)** | Cluster estremamente compatti e densi. | Genera una quantità enorme di Outliers. | **Configurazione 2:** Oltre la metà dei dati (53.34%) è considerata "rumore". |

### Considerazioni Geometriche
* **Distanza Coseno (`cosine`) vs Euclidea (`euclidean`):** Nei dati testuali ad alta dimensionalità (embeddings dei Transformer), la distanza coseno è l'unica efficace perché valuta l'orientamento dei vettori (il contesto). In spazi ad alta dimensione, le distanze tra i punti tendono a diventare tutte simili, portando HDBSCAN a creare macro-cluster distorti dalle stopword.
* **Excess of Mass (`eom`) vs `leaf`:** Il metodo `eom` (Configurazione 1) recupera più documenti mantenendo il rumore più basso (34.57%), offrendo una copertura maggiore del dataset senza sacrificare la coerenza interna.
