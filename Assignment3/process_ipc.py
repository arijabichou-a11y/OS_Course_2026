import multiprocessing
import os
import time

def child_process(conn):
    """Fonction exécutée par le processus enfant."""
    child_pid = os.getpid()
    
    # 1. Recevoir les données du parent
    data = conn.recv()
    print(f"Child  [PID {child_pid}]: Received '{data}' from parent.")
    
    # 2. Transformer les données (Mise en majuscules)
    transformed_data = data.upper()
    time.sleep(1) # Simulation d'un petit traitement
    
    # 3. Renvoyer les données au parent
    print(f"Child  [PID {child_pid}]: Sending transformed data back...")
    conn.send(transformed_data)
    conn.close()

if __name__ == "__main__":
    parent_pid = os.getpid()
    print(f"Parent [PID {parent_pid}]: Starting application.")

    # Création du Pipe (duplex par défaut)
    parent_conn, child_conn = multiprocessing.Pipe()

    # Création du processus enfant
    p = multiprocessing.Process(target=child_process, args=(child_conn,))
    
    message = "hello from the parent process"
    
    print(f"Parent [PID {parent_pid}]: Sending '{message}' to child...")
    p.start() # Lance le processus enfant
    
    # Envoi de la donnée
    parent_conn.send(message)

    # Réception du résultat
    result = parent_conn.recv()
    print(f"Parent [PID {parent_pid}]: Received '{result}' from child.")

    p.join() # Attendre que l'enfant finisse
    print(f"Parent [PID {parent_pid}]: Task completed. Exiting.")