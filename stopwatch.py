import time
while True:
    for z in range(24):
        time.sleep(1)
        for t in range(60):
            time.sleep(1)
            for i in range(60):
                time.sleep(1)
                print("kronemetre",str(z).zfill(2),str(t).zfill(2),str(i).zfill(2))
    
    
    
    
    
