Metriikat k�yt�nteiden tukena ohjelmiston laadun arvioimisessa
 
Metriikat ovat yksi keino ohjelmiston laadun tutkimiseen. Niit� on paljon ja osa niist� on ollut k�yt�ss� kauan. Perinteiset mittarit perustuvat koodirivien m��r��n ja olio-ohjelmoinnin tapauksessa mm. metodien ja yliluokkien m��r��. Monet t�llaiset mittarit on havaittu tehokkaiksi virhealttiuden mittaamisessa. 

Metriikat voidaan jakaa ulkoisiin ja sis�isiin. Ulkoiset metriikat vastaavat ohjelmiston toimintaa ja 
sis�iset pohjautuvat ohjelmiston sis�isiin rakenteellisiin mittareihin. Laadunvarmistus tulee kohdistaa erityisesti niihin osiin ohjelmistossa, jotka metriikat ovat havainneet virhealttiiksi. Hy�dyllisiksi havaittuja metriikoita ovat muun muassa koodikirnu, verkkoanalyysi, testikattavuus ja mutaatiotestaus.

Koodikirnulla tarkoitetaan virhetiheyden ennakoimista muutosten m��r�� mittaamalla. Muutosten m��r� on saatavilla esimerkiksi versionhallintaj�rjestelm�n muutoshistoriasta. Koodikirnu koostuu joukosta suhteellisia mittoja, kuten yhteenlaskettujen koodirivien m��r�, tiedostojen muutokset ja tiedostojen m��r�. Ehdottomien mittojen perusteella lasketaan suhteelliset mitat, joiden on osoitettu korreloivan selv�sti virhem��rien kanssa.

Verkkoanalyysiss� komponenttien riippuvuudet esitet��n verkkona, jolloin niiden keskin�iset suhteet voidaan havaita helpommin. Analyysill� voidaan paikallistaa ohjelmiston paljon keskin�isi� riippuvuuksia sis�lt�v�t komponentit, jotka ovat yleens� muita virheherkempi�.

Testikattavuuden kasvulla ja julkaisun j�lkeisten virheilmoitusten v�henemisell� on havaittu selv� korrelaatio, mutta huomionarvoista on, ett� testien m��r�n kasvattaminen ei pienenn� samassa suhteessa virheiden m��r��. Testikattavuus ei kuitenkaan kerro testien laadusta. Yksi keino testien laadun arvioimiseen on mutaatiotestaus, jossa simuloidaan kehitt�jien tekemi� yleisimpi� virheit�. Valittuja mutantteja k�ytt�m�ll� ajetaan ohjelmiston testit ja katsotaan havaitsevatko testit v��r�n toiminnallisuuden.

My�s ohjelmistotuotantomenetelmill� on suuri merkitys hyv�ss� kehitysprosessissa, ne ovat laadukkaan kehitysty�n perusta. T�rke�� on havaita k�yt�nteet, joilla on olennainen yhteys ohjelmiston laatuun. T�m� n�k�kulma kuuluu olennaisesti ketteriin kehitysmenetelmiin.