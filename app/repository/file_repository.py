import dropbox

ACCESS_TOKEN = "sl.u.AFthWLtKwY7fjT3BRvoJOG2Gdzgad34oh3K3csI2vR1mOH67uZaBPq0DwbpCq6rHnn5v93KXxeKguHRHYzZ8hq63B1NRgAjYAYAr_E5wJFc1HD9EPrjnKaHYwhVxcCs-fPJjPjRSwIqic1Gwhu4KlKc1JXWnoFReb7dH4IMlAVFl-jfxpTPQE49j5HFwrnR8bO1nFEz3BHiTWCB2G_5FHMFWECkRB5ojkGnv6kbIt604On7fP3MqpDib4Y9eOhlaYmB6VQR7xvJoM6-ythV-LhfXysvQnOtJK5UIgBUUotsm5TNh9fc_CASfgh8_4muTgKE28MbNLpFG6PKjFut3VnRUlPWzplWSI5b2IHygAoNT6STwktBDfYkXp5YBMNmNxalbfLbigqqt0GlDPTfi4HY9Sz8mHsrlT9T41fjMoFT0DKVhF9XBcwEXCrjIWSRtWvuo4c3rqEFp0121TcIhsrQhA0bQhXuCAqwIP1OcvzXUOxH6g1P55pvCdDMnDOfwKEnXGzLts2atTI7CZeDOLkWlkjOWdzCyXMSpUI7AzxABYjPAHTEzRtxWy04VIivD_j3SqAvZr2Vjw04MD7mWLfCfHOlVzUBDypo2Nnmpo0hAVzjdQKendAZ_xNEW5jymZFV94bBiXk0MdeaKXYL9H_Kp7CiEmE7Jt8BoDDXOJFmCCAZ146rnpnW1LbDbjP03OYJ7XBT1LwxoFNW-aGwaY49Bt92VfaYwujKHM47ne-2_ir6ognB63lOFRP4ZC2n4zG3Nu8lwfn7zhfcFZMmFP7Lt22LAXa_NTC8lPYxzfmYwfGlrt-R5pbLZn1MGv9z8wQlugdm2_a2YKlxWqoDPx333Wj69D6rIVf1-dL2tvqL-ZM9nt0iiT-A2hYW-L9Gy2L487UnRbCSIope8ocDLH7WmIzDW2kLuY6YI4tkIuq6M9MSwC4C_wDWpzaAEDaZl0ErTlcq2bmBk_YeCnfdCZ9Zk56OVABpqpUYMGl0pxiSG4QP0m5xsekGGy0TPEhQRUJ_dteg7gCa1iyYnvBzbmdUl8nBSjeNAo2bHEcTHhC4ykNnmI4seNnSMjOSfbQ9y7oBc5ubsdyI_xEhh7Jyd6BGgJDCg1dcDCngDPdoB76koLvVdICkgssh0iMBbfVEFi2GTxrxScuhA-KndUeCMi5slxSDhWoHGrECVKd1oBYBPpcW9bHOwHYijinag3hiOazSH-_oyqfSPPvOEJ23R9poe_o4vAw75CNBGZU011tAkdRpyGxTiFWkq47nvwEv414aKJg1UG7jCawHOiIMPQkMpbRHozWMsiv8wIgawXwyZ3ObPSlDsgXMMwQSoii5dLZ3Ns-mghikGYMCdR812L47bRMsOoSMSTklicm6rKhzv2aWQbaWYGboPScRQPcjKyuMATq0yngBAIiU-7vF5scyAs0Gy6nTzxwSoj5OW7hrdeA"

def upload_to_dropbox(local_path: str, dropbox_path: str) -> str:
    try:
        dbx = dropbox.Dropbox(ACCESS_TOKEN)

        with open(local_path, "rb") as f:
            file_data = f.read()

        dbx.files_upload(
            file_data,
            dropbox_path,
            mode=dropbox.files.WriteMode("overwrite")
        )

        return dropbox_path
    except Exception as e:
        print(f"Error uploading file to Dropbox: {e}")
        raise

def get_dropbox_file_link(dropbox_path: str) -> str:
    try:
        dbx = dropbox.Dropbox(ACCESS_TOKEN)
        link = dbx.files_get_temporary_link(dropbox_path)
        return link.link
    except Exception as e:
        print(f"Error retrieving file link from Dropbox: {e}")
        raise