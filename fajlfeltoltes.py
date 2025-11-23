import random

with open("kamionok.txt", "w", encoding="utf-8")as file:
    file.write("kamionId;rendszam;teherbiras;fogyasztas;helyzet;kuldetes_idotartam")
    for i in range(1, 51):
        kamionId = i+100
        rendszam = f"{random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}-{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
        teherbiras = random.randint(10, 25)
        fogyasztas = round(random.uniform(20.0, 40.0), 1)
        helyzet = random.choice(["telephelyen", "kuldetesen", "kuldetesen", "kuldetesen"])
        if helyzet == "kuldetesen":
            kuldetes_idotartam = random.randint(1, 14)
        else:
            kuldetes_idotartam = 0

        file.write(f"\n{kamionId};{rendszam};{teherbiras};{fogyasztas};{helyzet};{kuldetes_idotartam}")