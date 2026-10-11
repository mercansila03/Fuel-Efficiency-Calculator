toplam_mil=0
toplam_galon=0

galon=float(input())
while(galon!=-1):
    mil=float(input())

    #depo başına mil/galon
    print(f"{mil/galon:.6f}")

    toplam_mil+=mil
    toplam_galon+=galon
    
    galon=float(input())

print(f"{toplam_mil/toplam_galon:.6f}")

    

