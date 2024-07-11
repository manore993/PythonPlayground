import csv
with open('Output.csv', 'w') as csvfile:
    with open('1000257 Grands livres du 01-01-2024 au  31-05-2024.csv', newline='', encoding='iso-8859-1') as f:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(["Compte", "Libellé du compte", "Journal", "Pièce", "Date","Contrepar.","Libellé Entête","Libellé Mouvement","Débit","Crédit","Solde","Lettrage"])

        reader = csv.reader(f, delimiter=';')
        
        account_name = ""
        account_number = ""
        for row in reader:
            if row[0].startswith("Compte"):
                account_number = row[0]
                account_name = row[1]
            elif row[0].startswith("Edition"):
                continue
            elif row[0].startswith("Total"):
                continue
            elif row[0].startswith("Date"):
                continue
            else:
                # ["", "", row[2], row[1], row[0], account_number, account_name, row[3], row[4], row[6], row[7], row[5]]
                # writer.writerow([account_number, account_name] + row)
                writer.writerow(["", "", row[2], row[1], row[0], account_number, account_name, row[3], row[4], row[6], row[7], row[5]])
                print(f"{account_number};{account_name};{row}")
            # print(row)


    



