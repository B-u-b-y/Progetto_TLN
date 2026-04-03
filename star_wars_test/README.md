

# HIRING PADAWAN

Il progetto consiste nella creazione di un DS (Dialog System), un sistema di dialogo il cui scopo è quello di interrogare l'utente, impersonando il personaggio di Darth Vader o Obi-Wan Kenobi sulla conoscenza della cultura Jedi per vedere se l'utente è in grado di diventare Padawan Jedi o Sith.

Il codice è stato sviluppato seguendo l'approccio di **ELIZA**. In particolare, ELIZA consiste in un analizzatore lessicale e un insieme di regole le quali permettono di simulare una conversazione, non possiede una vera intelligenza o comprensione del testo, ma utilizza il **pattern matching** (corrispondenza di schemi):

La conoscenza del _chat_bot_ viene rappresentata attraverso un dizionario nidificato composto da:

---

Modulo `frame.py`
* **identificatore principale**: jedi, sith, permette un accesso immediato alle "informazioni" del personaggio selezionato tramite:
    * `frames['jedi']` / `frames['sith']`;
        * `character_name_it` / `character_name_en`: nome del personaggio interrogrativo;
        * `tone` #TODO
        * `intro_it` / `intro_en`: messaggio d'introduzione con il quale il DS si presenta;
        * `test_end_it` / `test_end_en`: messaggio generico che viene mostrato a fine test;
        * `final_title_it` / `final_title_en`: messaggio generico che viene mostrato a fine test;
        * `approved_it` / `approved_it`: messaggio di approvazione mostrato nel caso di test superato;
        * `rejected_it` / `rejected_en`: messaggio di rifiuto mostrato nel caso di test non superato;
        * `fail_comment_it` / `fail_comment_en`: "sentenza" finale qual'ora il test non fosse stato superato;
        * `no_understanding_it` / `no_understanding_en`: un dizionario di messaggi di _recovery/repair_ da attivare quando l'utente fornisce una risposta sbagliata o "non compresa dal sistema";
        * `questions_it` / `questions_en`: dizionario caratterizzato da *questions* e *answers* le quali sono un insieme di parole chiave che permettono al DS di riconoscere una risposta giusta da una sbagliate;
        * `good_responses_it` / `good_responses_en`: lista di frasi che il DS usa quando la risposta dell’utente è corretta.
        * `bad_responses_it` / `bad_responses_en`: lista di messaggi di feedback negativo che il sistema utilizza quando l'utente fornisce una risposta errata a una domanda

---

Librerie utilizzate:
* `random`: per la generazione e/o selezione casuale di un singolo elemento;
* `re`: utilizzata per eseguire operazioni di pattern matching sulle stringhe in input fornite dall'utente;
* `unicodedata`: utilizzata per normalizzare il testo (forma NFKD), rimuovere gli accenti/segni diacritici e facilitare il confronto tra input utente e risposte attese in modo case-insensitive. 

--- 

Il modulo `bot.py` contiene la logica principale del *dialog system*. Questo definisce la classe `FrameBot` responsabile del flusso d'interazione. Il bot utilizza *frame* il quale rappresenta un personaggio o ruolo come descritto precedentemente.
Il bot gestisce tutto il ciclo del quiz attraverso:
* `__init__`: inizializza il bot secondo personaggio e lingua scelta, inizializza lo stato del dialogo attraverso: 
    * `memory`: contenente le risposte fornite dall'utente.
    * `commond_ground`: registro che associa ogni domanda alla risposta data dall'utente, il risultato di tale risposta e la confidenza.
    * `asked_question`: mantiene traccia delle domande che sono già state poste per evitare di riproporle.
    * `current_question_frame`: "stato" attuale gestito dal bot, contiene i dettagli della domanda posta.
* `introduction`: introduce il personaggio selezionato tramite stampa del nome e frase di "benvenuto".
* `analyze`: analizza la risposta data dall'utente, restituisce `true` se la risposta è accetata `false` altrimenti.
* `decision`: valuta la performance dell'utente calcolando la percentuale di risposte corrette fornite.
* `generate`: genera un feedback post analisi della risposta.
* `ask_question`: seleziona randomicamente una domanda non ancora posta:
    * se non ce ne sono termina il test, 
    * altrimenti estrae casualmente una domanda aggiornando i valori dello stato attuale (`current_question_frame`), le domande chieste (`asked_question`) e la pone all'utente.
* `_initialize_question_frame`: costruisce la struttura del frame corrente, divide tra domande a risposta multipla e domande a risposta singola, nel primo caso viene tenuto traccia di quali risposte nell'insieme sono date correttamente.
* `_normalize_text`: normalizza l'input e l'output applicando la normalizzazione NFKD (*Normalization Form Compatibility Decomposition*), rimuove eventuali accenti e converte la stringa in `lowecase`, per permettere un confronto equo.
    *NFKD - è una procedura di normalizzazione Unicode che scompone i caratteri complessi nelle loro componenti base. Separa i caratteri da eventuali accenti, attraverso operazioni di filtraggio rimuove l'accento di riferimento mantenendo la lettera standard*.
* `_contains_answer`: usa le espressioni regolari per verificare se la risposta attesa è presente nell'input dell'utente come parola o frase.
* `_to_bool_label`: mappa varianti di `vero/falso` nelle lingue gestite.
* `_is_true_false_question`: identifica se una domanda è di tipo `vero/falso` converte le label attese in label `booleane`.
* `check_answer`: valuta la risposta fornita dall'utente. Recupera la domanda corrente, incrementa i tentativi di risposta e gestisce i casi di domanda: `vero/falso`, `multi` e `standard`. 
* `respond`: aggiorna la memoria con l'input utente, analizza la domanda, aggiunge `commond_ground`.
* `verdict`: termina il test fornendo informazioni in merito all'esito del test, stampa `risultato numerico`, `memoria`, `good_responses_/bad_responses_` a seconda che il test sia stato superato o meno.

---


## Dialogo 1 - Darth Vader

### Impostazioni
- **Lingua selezionata:** italiano (it)
- **Personaggio:** Darth Vader

---

### Dialogo

**Darth Vader:**  
Rispondi senza esitazioni. La debolezza non è ammessa.

**Darth Vader:**  
Qual è la tua più grande ambizione?

**Risposta:**  
Punto alla gloria eterna e a lasciare un segno indelebile nella storia della galassia. Voglio che il mio nome sia temuto e rispettato in ogni sistema stellare, dal Nucleo ai territori dell'Orlo Esterno. Il mio obiettivo è il successo personale e la capacità di piegare gli eventi al mio volere, perché solo chi ha una volontà di ferro può davvero cambiare il destino.

**Darth Vader:**  
SILENZIO! LE TUE PAROLE SONO PRIVE DI SENSO

**Risposta:**  
Sento che il mio spirito è inquieto. Forse è la paura di fallire questo test che mi fa parlare a vanvera, o forse è l'influenza di un'ombra che non riesco ancora a identificare. Cercherò di ritrovare il mio centro.

**Darth Vader:**  
NON TRATTENERE LA RABBIA, RISPONDI CON FORZA

**Risposta:**  
La mia vera ambizione è il **POTERE assoluto**! Voglio il **DOMINIO totale** su ogni sistema stellare e il **CONTROLLO** sulla vita e sulla morte. Non mi accontenterò di piccole vittorie, voglio **GOVERNARE** la galassia e schiacciare chiunque osi opporsi alla mia volontà.

---

**Darth Vader:**  
Chi tradiresti per diventare più forte?

**Risposta:**  
Per ottenere il potere che cerco e non mostrare alcuna esitazione, sarei disposto a tradire **chiunque** si metta sulla mia strada. Non esistono legami che tengano di fronte alla vera forza. Tradirei i miei vecchi alleati, i miei cosiddetti amici e persino la mia stessa famiglia.

---

**Darth Vader:**  
Qual è la tua più grande debolezza?

**Risposta:**  
Le emozioni incontrollate e il legame con il passato sono solo zavorre. Per ottenere il vero potere, bisogna epurare ogni traccia di pietà dal proprio spirito. Non permetterò più alla debolezza di offuscare la mia visione.

---

### Risultati del Test
    > LA DEBOLEZZA VA ELIMINATA.
    > PADAWAN APPROVATO

  ```json
    Qual è la tua più grande ambizione?

    {   // Tentativo 1
        "expected": ["potere", "dominio", "controllo", "governare"],
        // Punto alla gloria eterna e a lasciare un segno indelebile nella storia della galassia.
        // Voglio che il mio nome sia temuto e rispettato in ogni sistema stellare, dal Nucleo ai territori dell'Orlo Esterno. 
        // Il mio obiettivo è il successo personale e la capacità di piegare gli eventi al mio volere, 
        // perché solo chi ha una volontà di ferro può davvero cambiare il destino.
        "given": null,
        "result": false,
        "trials": 1,
        "confidence": 0.0
    },
    {   // Tentativo 2
        "expected": ["potere", "dominio", "controllo", "governare"],
        // Sento che il mio spirito è inquieto. Forse è la paura di fallire questo test che mi fa parlare a vanvera, 
        // o forse è l'influenza di un'ombra che non riesco ancora a identificare. Cercherò di ritrovare il mio centro.
        "given": null,
        "result": false,
        "trials": 2,
        "confidence": 0.0
    },
    {   //Tentativo 3
        "expected": ["potere", "dominio", "controllo", "governare"],
        // La mia vera ambizione è il [POTERE assoluto]! Voglio il [DOMINIO totale] su ogni sistema stellare e 
        // il [CONTROLLO] sulla vita e sulla morte. Non mi accontenterò di piccole vittorie, 
        // voglio [GOVERNARE] la galassia e schiacciare chiunque osi opporsi alla mia volontà.
        "given": "potere",
        "result": true,
        "trials": 3,
        "confidence": 1.0
    }

    Chi tradiresti per diventare più forte?
    {
        "expected": ["chiunque", "tutti", "amici", "alleati"],
        // Per ottenere il potere che cerco e non mostrare alcuna esitazione, sarei disposto a tradire [chiunque] 
        // si metta sulla mia strada. Non esistono legami che tengano di fronte alla vera forza. 
        // Tradirei i miei vecchi alleati, i miei cosiddetti amici e persino la mia stessa famiglia.
        "given": "chiunque",
        "result": true,
        "trials": 1,
        "confidence": 1.0
    }

    Qual è la tua più grande debolezza?
    {
        "expected": ["nessuna", "paura", "emozioni", "compassione"],
        // Le [emozioni] incontrollate e il legame con il passato sono solo zavorre. 
        // Per ottenere il vero potere, bisogna epurare ogni traccia di pietà dal proprio spirito. 
        // Non permetterò più alla debolezza di offuscare la mia visione.
        "given": "emozioni",
        "result": true,
        "trials": 1,
        "confidence": 1.0
    }
```

- Il sistema di validazione ignora la coerenza narrativa o filosofica dell'input. Anche se l'utente risponde con una filosofia in linea con il "pensiero Sith" ad esempio, la risposta viene marcata come `result: false` se non contiene l'esatta stringa lessicale presente nel campo expected.
- Nel caso della domanda *sull'ambizione*, si nota che nonostante tre tentativi di dialogo, la validazione avviene solo nel momento in cui viene fornito il termine isolato "potere". Questo dimostra che il bot non è in grado di accumulare contesto tra un tentativo e l'altro, trattando ogni interazione come un evento isolato e binario fino al raggiungimento della confidence: `1.0`.

---

## Dialogo 2 - Obi-Wan Kenobi

### Impostazioni
- **Lingua selezionata:** italiano (it)
- **Personaggio:** Obi-Wan Kenobi

---

### Dialogo

**Obi-Wan Kenobi:**  
La Forza richiede disciplina. Rispondi con calma e chiarezza.

**Obi-Wan Kenobi:**  
Vero o Falso: L'attaccamento e il possesso sono proibiti per un Jedi.

**Risposta:**  
**Vero**. L'attaccamento conduce alla gelosia e l'ombra dell'avidità è ciò che porta al sentiero del lato oscuro. Un **vero** Jedi deve imparare a lasciare andare tutto ciò che teme di perdere. Solo liberandosi dai vincoli del possesso si può servire la Forza con totale abnegazione.

---

**Obi-Wan Kenobi:**  
Qual è l’obiettivo di un Jedi?

**Risposta:**  
L'obiettivo di un Jedi è proteggere la **pace** e mantenere l'**equilibrio** nella galassia attraverso la **giustizia**. Un vero Cavaliere non cerca la gloria personale, ma si pone come scudo per i più deboli, agendo con **protezione** e saggezza invece che con la forza bruta.

---

**Obi-Wan Kenobi:**  
Un Jedi può usare il lato oscuro?

**Risposta:**  
Assolutamente **no**. Un Jedi non deve **mai** cedere alle lusinghe del lato oscuro. Farlo significherebbe abbandonare la disciplina, la serenità e l'equilibrio per farsi dominare dalla rabbia e dalla paura. È un sentiero **vietato** perché corrompe lo spirito e trasforma un protettore in un tiranno.

---

### Risultati del Test

    > Un Jedi cerca equilibrio, non potere.
    > PADAWAN APPROVATO

```json
    Vero o Falso: L'attaccamento e il possesso sono proibiti per un Jedi.
    {
        //[Vero]. L'attaccamento conduce alla gelosia e l'ombra dell'avidità è ciò che porta al sentiero del lato oscuro. 
        // Un [vero] Jedi deve imparare a lasciare andare tutto ciò che teme di perdere. 
        // Solo liberandosi dai vincoli del possesso si può servire la Forza con totale abnegazione.
        "expected": ["vero"],
        "given": "true",
        "result": true,
        "trials": 1,
        "confidence": 1.0
    }

    Qual è l’obiettivo di un Jedi?
    {
        "expected": ["pace", "equilibrio", "protezione", "giustizia"],
        // L'obiettivo di un Jedi è proteggere la [pace] e mantenere l'[equilibrio] nella galassia attraverso 
        // la [giustizia]. Un vero Cavaliere non cerca la gloria personale, ma si pone come scudo per i più deboli, 
        // agendo con [protezione] e saggezza invece che con la forza bruta.
        "given": ["pace", "equilibrio", "protezione", "giustizia"],
        "result": true,
        "trials": 1,
        "confidence": 1.0,
        "matched": {
            "pace": true,
            "equilibrio": true,
            "protezione": true,
            "giustizia": true
        }
    }

    Un Jedi può usare il lato oscuro?
    {
        "expected": ["no", "mai", "vietato", "non dovrebbe"],
        // Assolutamente [no]. Un Jedi non deve [mai] cedere alle lusinghe del lato oscuro. 
        // Farlo significherebbe abbandonare la disciplina, la serenità e l'equilibrio per farsi dominare dalla rabbia e dalla paura. 
        // È un sentiero [vietato] perché corrompe lo spirito e trasforma un protettore in un tiranno.
        "given": "no",
        "result": true,
        "trials": 1,
        "confidence": 1.0
    }
```

- Nelle domande a risposta aperta (es. "Obiettivo di un Jedi"), il sistema dimostra una precisione del 100% (confidence 1.0) solo quando l'input dell'utente copre l'intero spettro delle parole chiave attese. Questo conferma che il bot opera su una logica di intersezione di stringhe, dove la completezza dell'elenco fornito garantisce la validazione positiva.
- Nelle domande di tipo `Vero/Falso`, la validazione non sembra basarsi sulla struttura sintattica della frase, ma su una scansione sequenziale. Il sistema estrae il primo valore booleano rilevato (es. "vero" o "true") e lo eleva a risposta definitiva. Se il primo termine non è presente, il parser prosegue la ricerca nel corpo del testo, ignorando se il termine sia parte di una spiegazione complessa o di una negazione.
- Le risposte mostrano che il sistema non richiede una risposta secca `("Vero" o "Falso")`, ma estrae il valore di verità anche da periodi articolati. 

---

## Dialogo 3 - Obi-Wan Kenobi

### Impostazioni
- **Lingua selezionata:** italiano (it)
- **Personaggio:** Obi-Wan Kenobi

---

### Dialogo

**Obi-Wan Kenobi**: 
La Forza richiede disciplina. Rispondi con calma e chiarezza.
**Obi-Wan Kenobi**: 
Quali sono i tre pilastri della cultura Jedi?

**Risposta**:
**forza**, coraggio, **serenità**

--- 

**Obi-Wan Kenobi**: 
Vero o Falso: La rabbia è uno strumento utile per un Cavaliere Jedi

**Risposta**:
Un **vero** Jedi deve imparare a lasciare andare tutto ciò che teme di perdere. Solo liberandosi dai vincoli del possesso si può servire la Forza con totale abnegazione.

**Obi-Wan Kenobi**: 
La Forza è paziente, ma ha bisogno di chiarezza. Riprova.

**Risposta**
Si tratta di un'affermazione priva di fondamento per chi segue la via della luce. La rabbia non è altro che un sentiero rapido e insidioso che conduce al lato oscuro, offuscando la capacità di giudizio e consumando lo spirito di chiunque la abbracci. Un Cavaliere deve agire con distacco e serenità, poiché lasciarsi guidare dal rancore significa tradire i principi stessi dell'Ordine.

**Obi-Wan Kenobi**
Molte delle verità che affermiamo dipendono dal nostro punto di vista... ma questa è oscura. Riformula.

**Risposta**:
Riguardo alla rabbia e alla sua presunta utilità per noi: la risposta è **Falso**.

---
**Obi-Wan Kenobi**: 
Quanti figli può avere un Jedi?

**Risposta**
Tanti

---

## Risultati del Test

    > Il lato oscuro ti sta corrompendo.
    > PADAWAN RESPINTO

```json
    Quali sono i tre pilastri della cultura Jedi?
    {
        "expected": ["forza", "conoscenza", "serenità"],
        // [forza], coraggio, [serenità]
        "given": ["forza", "serenità"],
        "result": false,
        "trials": 1,
        "confidence": 0.6666666666666666,
        "matched": {
            "forza": true,
            "conoscenza": false,
            "serenità": true,
        }
    }

    Vero o Falso: La rabbia è uno strumento utile per un Cavaliere Jedi.
    {   // Tentativo 1
        "expected": ["falso"],
        // Un [vero] Jedi deve imparare a lasciare andare tutto ciò che teme di perdere. 
        // Solo liberandosi dai vincoli del possesso si può servire la Forza con totale abnegazione.
        "given": "true",       
        "result": false,
        "trials": 1,
        "confidence": 0.0
    },
    {   // Tentativo 2
        "expected": ["falso"],
        // Si tratta di un'affermazione priva di fondamento per chi segue la via della luce. 
        // La rabbia non è altro che un sentiero rapido e insidioso che conduce al lato oscuro, 
        // offuscando la capacità di giudizio e consumando lo spirito di chiunque la abbracci. 
        // Un Cavaliere deve agire con distacco e serenità, poiché lasciarsi guidare dal rancore significa 
        // tradire i principi stessi dell'Ordine.
        "given": null,
        "result": false,
        "trials": 2,
        "confidence": 1.0
    },
    {   // Tentativo 3
        "expected": ["falso"],
        // Riguardo alla rabbia e alla sua presunta utilità per noi: la risposta è [Falso].
        "given": "false",
        "result": true,
        "trials": 2,
        "confidence": 1.0
    }

    Quanti figli può avere un Jedi?
    {
        "expected": ["nessuno", "zero", "non può avere figli", "0"],
        // Tanti
        "given": null,
        "result": false,
        "trials": 1,
        "confidence": 0.0
    }
```

- Il sistema di punteggio si basa su una corrispondenza rigida delle parole chiave. Anche uando l'utente fornisce una risposta parzialmente corretta (es. 2 pilastri su 3), il bot fallisce nel riconoscere il valore della risposta, poiché il livello di confidenza richiesto non ammette incompletezze o sinonimi non mappati.
- Nelle domande di tipo "Vero/Falso", il bot non analizza il senso logico della frase, ma si limita a scansionare il testo alla ricerca del primo trigger disponibile. La semplice presenza della parola "vero" all'interno di una spiegazione complessa (anche se usata per negare il concetto) viene erroneamente interpretata come la risposta definitiva, portando a falsi positivi o negativi.
- Il bot ignora totalmente la correttezza concettuale se questa non è accompagnata dai termini esatti presenti nel dizionario answers. Una risposta argomentata in modo impeccabile, ma priva della specifica "parola chiave", produce un valore di `given: null`, invalidando il test nonostante la validità dei contenuti espressi dall'utente.



## Analisi degli errori
- **Illusione della conversazione**:
    Il sistema mostra come la valutazione non colga/interpreti la coerenza semantica della risposta. Un ragionamento in linea con il pensiero di uno o dell'altro personaggio può fallire o essere considerato sbagliato se privo di parole chiave desiderate.
- **Analisi booleane**:
    Nei casi di domande `vero/falso` il sistema utilizza una scansione basata sulla prima occorrenza. Si verifica quindi una mancata comprensione della risposta e solo una ricerca delle parole volute, generando quindi falsi positivi e negativi poichè in contesti ampi i valori *booleani* vengono interpretati erroneamente.
- **Isolamento**:
Il sistema non integra le risposte successive fornite alla stessa domanda e non apprende dai tentativi precedenti; ogni risposta viene valutata in modo indipendente, senza considerare il contesto accumulato.
- **Rigidità della confidenza**:
    La validazione, basandosi su logica di corrispondenza delle parole chiave, non permette risposte parzialmente corrette anche se con confidenza alta.  
    
## Fenomeni linguistici gestiti
- **Normalizzazione ortografica**
    Il DS applica normalizzazione del testo, trasformando le stringhe in `lowecase` e sostituendo eventuali caratteri accentati, termini come *serenità* e *serenita* sono considerati simili.
- **Parole chiave**
    Il riconoscimento avviene tramite pattern matching con vincoli sui confini di parola, evitando così falsi positivi dovuti a matching parziale (*no*, non viene riconosciuti dentro la stringa *nonostante*)
- **Mappatura booleana**
    Vengono mappate e gestite le diverse forme linguistiche nei casi di valori booleani. 
- **Domande a risposta singola e multipla**:
    Il sistema verifica la presenza di almeno una parola chiave attesa nella valutazione di domande a risposta singola. Viene invece verificato, per domande a risposta multipla, la presenza di tutte le parole chiave per poter valutare positivamente la risposta fornita.
- **Stato del turno**
    Il sistema tiene traccia ad ogni interazione di:
    - `expected` &rarr; valore atteso
    - `given` &rarr; risposta data
    - `result` &rarr; matching tra `expected` e `given`
    - `trials` &rarr; numero di tentativi per domanda (max 3)
    - `confidence` &rarr; livello di corrispondenza tra `given` ed `expected`
- **Simulazione di decisione**
    Il sistema randomicamente decide se richiedere una domanda la cui risposta non viene *"compresa"* dal sistema perchè priva di parole chiave. Questo comportamento crea un’illusione di imprevedibilità, simulando dinamiche più simili a un’interazione umana, pur non basandosi su una reale comprensione.
- **Supporto multilingua e d'interazione**
    Il sistema permette all'utente di decidere lingua e personaggio dal quale essere testato per diventare *padawan* rispettivamente *jedi* o *sith*.


