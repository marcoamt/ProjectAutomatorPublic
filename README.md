# Project Automator
Automatizzazione della creazione della repo di un progetto e relativo salvataggio in una cartella nel Mac

# Caratteristiche
Abbiamo 2 file:

## .custom_commands.sh
Questo file serve per creare un commando "Create" utilizzabile dal terminale Mac. 
Ad esempio: Create Flutter NewApp
Nella funzione create $1 = Flutter e $2 = NewApp
Alla chiamata per l'esecuzione di Automator.py verrà passato il nome della repo $2 mentre $1 servirà per posizionarci nel nostro caso nella cartella FlutterProjects dove verrà creata la nuova cartella per il progetto e collegata alla repo creata da Automator.py

## Automator-py
Permette la creazione della repo su github dopo essere stata chiamata dal comando Create.
Si dovrà dare username e password di github per la creazione della repo.

# Dipendenze
Bisogna installare PyGitHub: $ pip install PyGithub
Per quanto riguarda il file .sh seguire la guida https://medium.com/devnetwork/how-to-create-your-own-custom-terminal-commands-c5008782a78e
