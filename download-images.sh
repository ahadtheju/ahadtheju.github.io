#!/usr/bin/env bash
# Downloads the 26 photos from the old Google Site into ./images with the
# filenames the pages expect. Run this once, from inside the site folder:
#
#     bash download-images.sh
#
# It needs `curl`, which macOS and Linux already have. On Windows, use Git Bash
# or WSL, or just save the images by hand using images/PHOTOS.md as the guide.
#
# The URLs are Google Sites' own copies. They work while the old site exists.
# If any download comes back tiny or broken, open the old site, right-click the
# photo, "Save image as", and use the filename from images/PHOTOS.md.

set -u
mkdir -p images
ok=0
fail=0

get () {   # get <filename> <url>
  local out="images/$1"; shift
  local url="$1"
  if curl -fsSL --max-time 60 -o "$out" "$url"; then
    # a Google error page is a few hundred bytes; a real photo is not
    local size
    size=$(wc -c < "$out")
    if [ "$size" -lt 2000 ]; then
      echo "  SUSPICIOUS (${size} bytes): $out - check this one by hand"
      fail=$((fail+1))
    else
      echo "  ok: $out (${size} bytes)"
      ok=$((ok+1))
    fi
  else
    echo "  FAILED: $out"
    fail=$((fail+1))
  fi
}

echo "Events and schedule"
get events-day1.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQVGntwhYJDOOi7E0r_8bcaeSx6TiaYAvQvgFTKOUtPwZUDgxLhaK1AEJFJUB7SjzU0ilolDzjGTrwgEg0yPF25gLundnKNONzxyXZrcjW0JatnpSBVC98De8YrV7uxDj7L88JmVSuJa60_G2t34kIcJCqWWQb8sERVBcDIXXopxdgS8nq6j42dDGxUnTrRg2lureDZYGrehDZ6WJhJ1VOszrKmgI_7_s_hVm2gE=w1600"
get events-day2.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQV9_tiboO4t9Oyen6AWnCbxVyzNAjXnZnS4_Uw7pZ4LBoVD8gBp3tGDvv9zo9q9B9j5RDy7nFFY98bXfb2h9iNeOXWfDpeM5pnU3VIkl1awA-JbDEVdYtLGVcEVGSOPGwhzErO9ddolRo7GUXFNbLFcglUeIIHGJrQZUG979AL7487iv1JJTWvCTLWx_Wzg2ScioTirLw4_tm3MhxNdEINpx7EAIt_I68KRmprAfbA=w1600"
get events-afterparty.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQUtC2F9qusvix0PkOt4jBiAFe5dO2alI-I8MSgp7GCuDkN_Z6xxWW2GWDEz5rFTytySa1zTqLu-ufwEBvJQIOECrvmGKigzyVg5me66B3GhzaBTERcHAgFjWrWzCSzLdtDv-bujPXmKfLsyejvrunlUYwREhKJQwk1RirC8Vzhwq7DKWjCjp0wA5VVewdm9LrVtE851vv7_1xbdb7Fb82JCKujiVg49DNmvKpnu=w1600"

echo "Stay"
get stay-keys-prima.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQVpexTpbEAkV2t1uxl0QcbbNAiizNnpCkilCn9dM8SZhrVqyplfAj-bpYjzz5-d5_UqvmQPuqJyAKetBLBObVg366o3yw_a69DT4a_MK0gWmsTPMcod5OH9PCXYfLfE4PnbS093Q0WQK6UXWMK-6CVMCPy75gjAN-fAGyMCas1syCO2N7wnhpilkcWY8fGyLenVA2kQ3o1tEwVMk4IuztMIOZrAFUk4Usw9URCyeTM=w1600"
get stay-cmi.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQXZXshNa5IFsbj8Owo-3PBFPh5UqgopN8FoddIRv7J-YOg7qhUx9nUu-KwnsQLBL5DjMwcgjttDbWTEo8ZYCl1znwSTeLvS43-4mnn-e9g59WXAYjmRo8nYJF5_NjCayAWPH1fkwZq943g5Kmrig0wYg1jiZL7UVRxGJnWdz52BCS4w1Jph4LKa6Am1Vmt_ZiITFUW9lkVeoEVrL5h0CFjS-ihs9ZBrqOCEtGxi=w1600"
get stay-airbnb.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQWPNJ_LwV5heMdNCBrwy190VU_4trVsY3qBLHWLlkcgqBpPUa0l43nUsFa2mDvJD2m-CXsB8rbomxNOHYWzK_bRblGTppOX2SDCVjwv4zC9okB9ob-ikYINKrDg_QvMTAMndCm3oNVRA0FDQMMDE0vZN8tb8O6oQKbmVgFnXIjvF7qDb2Pe61d7MHPiYRhS1dndxEr5G4maAbHLORsh_sqaQSDSg5VTVmXb_yioYLU=w1600"

echo "Attire (FAQs page)"
get attire-saree.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQXHdkbx_9X_3hZ1vmbIuWiHv6u1RXBv1Bdij2SJgPSEcJxX7GGuhWGyuGPYokrinukl9Kqwsi3G9oQ8xAZVkkqNPuGUP6g6FUgoDPw4kja_tIEpaDLoeBuK8FzGoc54e6UDvWAk-NPDOz2hV2BLB1XkGa1Rb8wagB7uN0MAJRwkeF9cjptyQOu7O1zT8AKjzPgBOOpHpMv04UlQMWkKxzWPiQbSEZLEnwIAaLQbHtU=w1600"
get attire-kurtha.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQX7bTrRljprSLi1CwrQZPT9seMBruyShnxUhQBpR3yXS8J-ueqb-yjqKmR6vnIwpHf1eB6wEWTgy0jHAxjYyEQK7BN4b7tHJO1MyFHSVoo5u6SuqB3brVY27fG9uc4i-Xhc2XsY1QFaDy5cHxRCotdLCvsy8H31IssGJ7aZd0Kd2jBjTiXdkFrq0smPnElstmPIpEBnEQ2tp9eLElEVaXcMZYKoovqzpKZpKSx1rX0=w1600"
get attire-lehenga.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQVfcz-qxC2_r0bcSXlUvjzjyvZgn2gulP7IR8atiM80JywqBP2WNknM3t28SuJFTCOis5ZP7mV6gaYxZxPzYjDiGoma1_ed-pOGuzNVUlQ9CS2qD25k05BHsHZLcpI2K01zv10KwqbWpiem4wdznqhn5C6bLD7DogKUWb0WL6_7gBplpyNkSUDKxyXteMOqYs0AgZ87kLZCbnBh0cZ9zqJVidDbFuScSA3yCh2mxn0=w1600"
get attire-salwar.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQXg7YxiXkne9ujT934log8_82iboSSBz7F_3Eg4dhCuy-Ug3bull9NVnfjGCdYsTUBfidvw2WVZYA1DetT3fja_-OyCkQEwP3i-BaDs5EOXl1VJGjsdSDrMkISo51_pzUbDAigB4Mw3wKeHVLUwuxd_zF_o0WwgxnJUAyeAjOPfRhf14lc6eHcIV95hycERz0nRJt3BDlRvPPpaN3JmyVXTlevI3iDNqu6rPYC1y1I=w1600"
get attire-dhoti.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQVJybFqsQA4Nuiu1oQ125LjYziYLrchBGPWB3Bg8FtjSyzv5HnEmeoOg62-kBJq4ydJdfOkyHWfDX94aDfSqoroI-hg-2ES34gwRkWM7ksweQiM7JjQF1RASuDrucF6OnpcntcAseaoQfLVt97QfCNjekOMM03W2WeuAzC9yFhCbiCmKMjyJUFUL3obEHyl-kFnZGNG9Cbc-HKOA2wNxwKOABsLLM_FLgfLmteL=w1600"
get attire-anything-else.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQXHlGiS_yy3Ac4F0UVpo017fGd-HJuW3zpjoD15lTAqjklpyAbrk6TYyHNEQ-Qidq92SWZQ24YP0sfkmmyP8Vx9R10nBTetUF-HfuPCEEVX0m3JyATKrdOIL2C6KiuCsPOnWT5LeECPxk-Wz5WrQwV0pMllcuaBlHekTlU1kTiGpsoEVNAK4tmNyBACeK7rpxmxerVJlH_DdQK9_YJNp69tGpjQoltbiAKxYuQ-0uQ=w1600"

echo "Places to visit"
get place-dakshinachitra.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQVH8pRDYZr3P4V51lzAH9ef4X2_jVO6yRwwFtzdoIkHTSeE_3aDgViwnr0PLfIQ0nWpueqT-MgtCWj3p6P2IKO8YeDRwTmMMqB1ExsyPb2yIbg37Cia4rJXZY_xqnlL8hj_GhsDMh76sIlzcKVOOSFK5yNHAouW7OcGY3YL6Eb58kGeRjHbZD5W0bUEhU5Tc94cRNsurmWarieGNmeNh_hFbwPVPXc7P6ricav4=w1600"
get place-mahabalipuram.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQXDzG-MfT4MGj8r_No1emonGgOEj36umST-SYT_BUF4qWC6P5Gb7KbCcl1b_oFUz45DvV_0fjBolFcardbCe8EvFIDMNkR6QvATu1jqX2JtF494JIY1A-KJGVZ2Pweudqq-gmadJ9O7jik964QukhiQ2fZsnwEDPP4vk1OV1xVT0Qb4-uU-W0Jb_yQC_Zzi-jEOmXmy1i21aJXrCwZyNQaJYvnR-FCMlpL-7_-UmeY=w1600"
get place-kapaleeshwarar.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQUgYivfZLJ-o_rRPi3FNKRNnCTVXdbw7_-KGc7AtiZTO8_F04gxnDTgaUJXWiN2w2XK9k8978giuv5g5J5jaurh1l9rWOL4QAXzhhyr2qPVxI679Dm_WNyOkPjrEtIdskgH-TqV09b5RDOFEed9QM-BhmmoGWry1LuChSVbU2xPFNvy6qpJOgjjAN63gCKqGuzjoE6cSYawFWvaFR7jz1pbe5IPNml5Hu8eyo0lzyU=w1600"

echo "Food recs"
get food-annalakshmi.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQUrVA5Scrt1vktTCoEjGA-WiMp4F_GeNcCTCUFh9lHIsiigv0Ia7jTRhMeXxXcFQcmJkLFvz4wIvJgtxkozypPs1UcNsRgCS6Kf2miEPK9dpeY71hw3rpNVoI9JKENCsl5d--0l4HhlZ8t5uJy4-u3nyxwK8i6ysCoMQFveoxEWzqB0W33ct4HH7AGQq6r9goTcVQWylP1hsSZIkyGvGwedB6wzLf2VUyJ_9e23qdc=w1600"
get food-the-farm.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQVMrbgV_wo-fM12jqRqKOswq6UQx2G71Dr9mLiCc59Cwsie7TnRRJb-UmXCVHBakTcrwkZX8eXTGIBYu0uX7XmULD9ilSdSY9Rbr52R6V9RgnnjfF9l5V6vJviwfDSVSi_10oBMeNeXXZvIi-QhUs9OAoebIcNB68-0glSnejbSUi3QpG7h-CK0iAp97BVm_vqY-dntI3EQIMpqjQLeB7_S-dYWF_5xzLPZNaqEm_Y=w1600"
get food-kappa-chakka-kandhari.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQXQbq74eDdpOZG0UBqZ88QHqOMHSzwojzugPcjUEVVunMkvWomPq6RaezPV248OJXIkWT83SNLtuzE3r4ESHysbdEN0NIEMblazszKiyfBv0Umyzxvp1UvGDnbz77bHv4JimfESh4TmXf-0QaY06KS6YllN5hV7auK2e7OvlMxSN-JZc4O34jqxmdoxzIbTiIBmLPv8aRsT6jNf6moskKkVBx5dArLDIwv0h7nm=w1600"
get food-sandys.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQUUte5g39Kk_8xu5OCnOb-5ShBBvwxoLfjqfmkzigMgDMVAVwCqvUGtfS5ZPRJiU7fS33CilJBVNr5__GrGSUU6K_9P4bjht7tRgT_zEPVR4xwxPY3w3UNJXSO6CpfRkjiWbB7CGKwSqgpMIva3nim1zdcSlgylxnmJkFlQRN5owddc0qr4KGrfK3pDMJwRcdvfPS-8RLYso2R_7M8Gxz2nUiiRmscQnPKv37yzBII=w1600"
get food-kipling-cafe.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQW_GONeHVrAX0h44FfICKvZNgECgbM-ZmY_4R4oYPtQWikLgA6SqF6JlQ9l70_ML0-rXlEw2kc6AubJ3SDoKl0vOEv7JjQJLoX9MCkXUMaVzXjllRkJTmTCJcuIvlu-3pgsbFhCNyDZmvZngWes5tDJOKL4a68kHygp_HvHxc6bPALjIDXZf3kjeeFBulziv5gvfQ-B-7xhuU8Ny2GjkeLwdMWdAuk09BrZ1rxyWu0=w1600"
get food-murugan-idly-kadai.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQUt0KEmjwfFxwxvQmqHtcPxgzwXEtZjXAPZWFOTZAFOXsFBaP48ABCuks4M0_CShqxAuVCdlGVlmMJXM9rlZ0hlZyLn4jjcAL_xegGQObSsAggQEaXMfWPNX18WyCJ4DKFJgyTDNXkPGF5siiB32MawmmWpvepVJW9e6DJSBDTxsXHMqFs6sIbrWwn9AbZ6B245hngcKNeeVOIK0-ZNGed35L_iqopRy38IUL5f=w1600"

echo "Other places in south India"
get south-kerala.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQUbWWV4G5j8JCkfK5NYBqnRv0pDb7NszuyKGa2Cyw9psYkjqCi9e9Rzsgqj4V4DVjad2Yz89rgdmD6ommcBbLpRj7AyJTsTD6Wb3MHiSQnYY4Zlezo89kKhQ5BVBsrHe0Cn9-Saydc4E0HVSAEBOlDBQOuPXMHINH9VSO9a7fRHWLbvTcFtmw_dhD9SJR_8nHH4CfH2ba0vVPor5lTjhfNmfb4A4UO0IV9TOgumH5g=w1600"
get south-goa.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQUNdr255Ym42bh2RYw118-B4mkwxrW8eDZYt_6MyRYgwIhTjmw6wOCXgJbzf0tywNvcqM3_yzkfALWFFNfhaOnQVc1BtVivz5eibKolV4RVIuNNxsfXLKD4KMoj3NrD6jUBDCME6YkdOqnZCA98K9C2wqDwW6LFxeajhMrWm8-EAdm8Via78cHBaYbRJDM0nJKb0SaOp_apMtcTL64hmarcXttCIOJtPHXdHDvB=w1600"
get south-hyderabad.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQXz8k5Yn21RV8y96TtZoRiAVJXJ5fWutQ_-xMrZNzB6HlELVSQQJorVlT_f1FCxrHYzF0uYyTrF8XkUE7-M48AicNV3P9YHceFmyTDUj7b98JJz5ElfNYe32puE33iMYx2kKGS7WObpeS5Sm-TKeW8qfiPsj69wJceZ0WUqWbwAkzX-Erd4YZvbyl_dlmDP94Up6DL1Eh8F5CG3cd_RtmU2FukEhyoGf1w0kSVtkbU=w1600"
get south-ooty-kodaikanal.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQW_OHZkQxn91jiQh58wSQrwgyXaxvh_siJv7rZyuIIEqaArkq3OVGdmJZdQ6-xobqhUEHAgGmueL7pAHnnyqZYuoUtb24YmSsjVV-CXneqT2PR2bCtnyFf3hJxw9v1MI3w-mXG0ig96_f0G3WvMwNdcOPlF4qc5JQwxbq7edH-N4mlG7VLeIEgMsQLy7AJJ6-jYescd1rZoSDQcX-uusRCm5r1D-hhCQWgG=w1600"

echo "Colocated events"
get colocated-cmi.jpg "https://lh3.googleusercontent.com/sitesv/AG8ngQUPzDtIpydbGP_6390hTVZ4WNxzXVSAQrm9oMwQpnAGmUvIo1ylIBiy3wCPfeBelEVcpzLCJz9kN8psdOHFtsaZpvJX2pmKUd_sSzRCW5IJwKp3l653wRh7onceJFIAYVcH5hFA2mWv6jrfC2fkqD7-q45jzIpn5-RMkB9DkpSJx5LFjUbu29HQaw_P0kFzWdPF3eXlU4dtmYFN02UUsh5ThNFVOB4fMevjvEPttXY=w1600"

echo
echo "Done. $ok downloaded, $fail need a look."
echo "Open index.html and check that every photo is the one you expect."
