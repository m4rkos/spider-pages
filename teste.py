def repl_simbols(repl):
        
        n = repl.replace('Ç', 'C')
        n = n.replace('ç', 'c')
        n = n.replace('ã', 'a')
        n = n.replace('Ã', 'A')
        n = n.replace('õ', 'o')
        n = n.replace('Õ', 'O')
        n = n.replace('é', 'e')
        n = n.replace('É', 'E')
        n = n.replace('è', 'e')
        n = n.replace('È', 'E')
        n = n.replace('á', 'a')
        n = n.replace('Á', 'A')
        n = n.replace('à', 'a')
        n = n.replace('À', 'A')
        n = n.replace('â', 'a')
        n = n.replace('Â', 'A')
        n = n.replace('ô', 'o')
        n = n.replace('Ô', 'O')
        n = n.replace('ê', 'e')
        n = n.replace('Ê', 'E')
        n = n.replace('ü', 'u')
        n = n.replace('Ü', 'U')
        
        n = n.replace('å', 'a')
        n = n.replace('ä', 'a')
        n = n.replace('ö', 'o')
        n = n.replace('Å', 'A')
        n = n.replace('Ä', 'A')
        n = n.replace('Ö', 'O')
        
        n = " ".join(n.split())
        n = n.replace(' ', '-')

        res = str(n.lower())
        return res

print(repl_simbols("jghhfgh çkhjgjh"))