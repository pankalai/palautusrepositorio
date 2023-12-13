from luo_peli import Peli


def main():
    while True:
        print(
            "Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
        )

        vastaus = input()

        if not (
            vastaus.endswith("a") or vastaus.endswith("b") or vastaus.endswith("c")
        ):
            break

        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        peli = Peli.luo_peli(vastaus)
        peli.pelaa()


if __name__ == "__main__":
    main()
