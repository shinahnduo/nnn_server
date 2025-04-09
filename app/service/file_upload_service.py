import dropbox

ACCESS_TOKEN = "sl.u.AFr12vwFVZvfo5Eu742VnRKDfDtO7NbcajwDChn2Xv64EMLcXFN7aER65jUdiAPD41Vuu2dJc8ntXbXKpb7Fuu1_wJvX8-qLsK6YtOISkgrgMy7RIRWFwY6NPOIWJjd4PXQd9SMjf6ce2-R_fNbkPBtM8S9aLMsosJhbbS1mjbEm0stw7leHVjAq6o6ICJG--pHBqp7PB-KMucOkHFerS7UHZxewRMRalT8OtydXPDCW2iX_gn6VRNjr0xmpoKHYlcPzVqk8CZqp2ZSoFxUK9mKPIO8mrxsgTH8-Ew81Tdb7wE1QFLnyIDCTMuj-A5k84QgW8_mnPyzDYJAwAMi5khQlnhExmvSExvCe7GmUUKTSobRGTaluF6Dp1w3tMOH_XwPuXpluXsErrXDoPRuPOAqFmk9zcGnE_qdDPpkTNFkBsEweOZM1BfAXbhp3zGZKYuGBc2Kdwc93853RT2W2LoX90bnKUx6wxRrVFr2nFwDNJoviWUtCgNVjX6gGI_dZALpDmdAm1DNg3f-nPEpnIFuZSK6H0fN4enoaE40aOOB2LsvGUAXv31RmJm3GQyyY2M2uc5yWhPsKIMeCSbM3Rr_L4fD4YBJ8s7ejcKe54rdmmzA-uMVlGehG4VIDQcBHxUCFapqFSs5XXewxbij_UnBxqoziin91Frg9n90KUCCW9xfhwRt5U97SoqTxVhSwyeilUqTVbTshL__zcCgIughLAmLo8kaWi7078pVXFnVX_TY2H-mhgCuHpf2SiUk_LStyVC3y9qRsYu35URki0-OH2xWmL9XdPU8WOzRdhkJpm8KXeDXCo9WaaAvLLkz4CUCsbvFX7nFFjLdvUoXUtugfhrh1Ahjk-fbC4L1FcIlQ-gCbg47qOUmoDQzngj663E7SH6SFc-1k0li3xpkb5SmY1Oub_PaIglxuJB1-bQm5isGfWxuB6QAVPG_TVekJQieYLmh8BpiVDa5MO0Ec2F7UMNv_7-RNfeP00bBJToqiy1k4hlH1WBQ_TsG4CDLpQD10dxOBVjYKV1yYrrVuBaXSbKiLYL8YKyXfkAe4oOU_FTkNrr1a091aLpqno6R6ajmmLOx_WcGuvHIvweV3jrtkTdE-Qh-hTKEoxv3aMW3TeCdINZSW10HUtmkd3FTzoVmwknGEZAsXIj3W2NRctS1q_BTMBR3UslPIrEEu_0d6x7hAPAdAF-ZZ9tRQa5sfc_rDcetfBn7_JDoD3VTsSIXKRU3T4BJU9PZtjcNDyxAJaUosQBq3RyaWxeHDJvNUVW3D6Eh2XjU_cJHg7dPBkt_QIMp-F6N8zg4QmxNU0phU0qx9uab3hun0bcw2JN-Eti-dAmHYuCg3XqDanAf4K1ZMXOkPBrCQfZ1xoAAMN7iu5Hm48AvANe4dqjIDsVCzwH2Vkt1PC3o5jADReWWIgUEd"

def upload_file_to_dropbox(local_path: str, dropbox_path: str) -> str:
    try:
        dbx = dropbox.Dropbox(ACCESS_TOKEN)

        with open(local_path, "rb") as f:
            file_data = f.read()

        dbx.files_upload(
            file_data,
            dropbox_path,
            mode=dropbox.files.WriteMode("overwrite")
        )

        print("File uploaded successfully!")
        return dropbox_path
    except Exception as e:
        print(f"Error uploading file to Dropbox: {e}")
        raise