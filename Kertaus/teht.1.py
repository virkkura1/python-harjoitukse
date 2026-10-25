# if else harjoitus

tuntipalkka = float(input("\nAnna tuntipalkka?:"))
tunnit = float(input("\nAnna tunnit?"))
viikonpaiva= input("\nAnna viikonpäivä?")

if viikonpaiva == "sunnuntai":
    paivapalkka =  2 * tuntipalkka * tunnit
    print(f"Päiväpalkka on: {paivapalkka} euroa")

else:
    paivapalkka = tuntipalkka * tunnit
    print(f"Päiväpalkka on:{paivapalkka} euroa")