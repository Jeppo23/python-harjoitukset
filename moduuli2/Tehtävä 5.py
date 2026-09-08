leiviska = float (input ("montako leiviskaa? "))
naula = float (input("montako naulaa? "))
luoti = float (input("montako luotia? "))

leiviska_grammoina = leiviska * 20 * 32 * 13.3
naula_grammoina = naula * 32 * 13.3
luoti_grammoina = luoti * 13.3

grammat = leiviska_grammoina + naula_grammoina + luoti_grammoina

kilot = grammat // 1000
grammat_jaljella = grammat % 1000
print("Massa on", kilot, "kg ja", grammat_jaljella, "g")
