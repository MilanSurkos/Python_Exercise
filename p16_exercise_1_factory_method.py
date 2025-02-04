"""Factory Method – Správa uživatelů v aplikaci
Vytvoř aplikaci pro správu uživatelů, kde budou různé typy uživatelů
(např. Admin, Editor, Viewer).
Použij návrhový vzor Factory Method, aby bylo možné snadno vytvářet instance
těchto uživatelů na základě vstupního parametru.

Požadavky:
- Každý typ uživatele by měl mít specifické oprávnění
(např. Admin může upravovat vše, Editor jen články, Viewer jen číst).
- Použij polymorfismus – každý uživatel bude mít metodu get_permissions(),
která vrátí jeho oprávnění.
-Implementuj tovární metodu UserFactory.create_user(user_type)."""