Metriikat käytänteiden tukena ohjelmiston laadun arvioimisessa
 
Metriikat ovat yksi keino ohjelmiston laadun tutkimiseen. Niitä on paljon ja osa niistä on ollut käytössä kauan. Perinteiset mittarit perustuvat koodirivien määrään ja olio-ohjelmoinnin tapauksessa mm. metodien ja yliluokkien määrää. Monet tällaiset mittarit on havaittu tehokkaiksi virhealttiuden mittaamisessa. 

Metriikat voidaan jakaa ulkoisiin ja sisäisiin. Ulkoiset metriikat vastaavat ohjelmiston toimintaa ja 
sisäiset pohjautuvat ohjelmiston sisäisiin rakenteellisiin mittareihin. Laadunvarmistus tulee kohdistaa erityisesti niihin osiin ohjelmistossa, jotka metriikat ovat havainneet virhealttiiksi. Hyödyllisiksi havaittuja metriikoita ovat muun muassa koodikirnu, verkkoanalyysi, testikattavuus ja mutaatiotestaus.

Koodikirnulla tarkoitetaan virhetiheyden ennakoimista muutosten määrää mittaamalla. Muutosten määrä on saatavilla esimerkiksi versionhallintajärjestelmän muutoshistoriasta. Koodikirnu koostuu joukosta suhteellisia mittoja, kuten yhteenlaskettujen koodirivien määrä, tiedostojen muutokset ja tiedostojen määrä. Ehdottomien mittojen perusteella lasketaan suhteelliset mitat, joiden on osoitettu korreloivan selvästi virhemäärien kanssa.

Verkkoanalyysissä komponenttien riippuvuudet esitetään verkkona, jolloin niiden keskinäiset suhteet voidaan havaita helpommin. Analyysillä voidaan paikallistaa ohjelmiston paljon keskinäisiä riippuvuuksia sisältävät komponentit, jotka ovat yleensä muita virheherkempiä.

Testikattavuuden kasvulla ja julkaisun jälkeisten virheilmoitusten vähenemisellä on havaittu selvä korrelaatio, mutta huomionarvoista on, että testien määrän kasvattaminen ei pienennä samassa suhteessa virheiden määrää. Testikattavuus ei kuitenkaan kerro testien laadusta. Yksi keino testien laadun arvioimiseen on mutaatiotestaus, jossa simuloidaan kehittäjien tekemiä yleisimpiä virheitä. Valittuja mutantteja käyttämällä ajetaan ohjelmiston testit ja katsotaan havaitsevatko testit väärän toiminnallisuuden.

Myös ohjelmistotuotantomenetelmillä on suuri merkitys hyvässä kehitysprosessissa, ne ovat laadukkaan kehitystyön perusta. Tärkeää on havaita käytänteet, joilla on olennainen yhteys ohjelmiston laatuun. Tämä näkökulma kuuluu olennaisesti ketteriin kehitysmenetelmiin.