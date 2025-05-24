import dropbox

ACCESS_TOKEN = "sl.u.AFpq03E3YiHrLTyuhw3tQ_EsiHSJm83LvJWCXDlWZc87TfAegaPDKFFuoBoveZD8x4ag8ZrKXrd8hfqTmzQM2dVhdttwiLtH10Cth8UOvuMR4pKRme9CuDgLmSUXE308klMr_yRGkdhyKjdzUWVw5yxKdYRZAiR4WabVfFBHYloAG1BTWmZol-ymiuWAMyb7oQDM9O324GrwSpkXCS1dIb6xiLdR0Ldohe5v78_rul0k3FqU1zPPofzi2nBO4bDmDCGf97Ou2Ky3Fj4CBNvdJMTsXbgRKDVPfSNhXt5ui8AUceKkBzZqeKNby0UIB0tPjr6G6LLeMrGFnbJ2AUWIlttyrBOMbia4AMwlyn5Wax76UqsNLLE0HmxRqZKI2U1_769iwb-JE4JCTY6hW9qMIfgDdmZfQQH1dkpeEPRll2ex8ikJhBlBKndDBCqlX1gIWf6xtxVTwge6dzoXiQ43VH2perla2mosGe9L_JODyW8zFG9E3aKdT3_l62uoVlCOVF5oNXQpGOAxm__AAQ2-XlUQhTfUE5wW__wAsCQD-dfWqw2aZ0WoExHbzUMBsUuF26eKfx-_1hv5LqkfMRxfkzuIHPrUVEncTxH1Ot2EnY57xJngZyH40YJZsCvTTOuOVXZuYxn7zs0pebuS62oq7m8dhAym-Q_ecy79kIAyK8eVpBUAVsHkJWyE4ME_0XbR7Xw9K6HIICsFybMJQS9idL4P2Av2CI6IMo5QXI9wuNQgwY58r5bQfc5VtRb5SGDXtiH9xQa7b87DWLM34eW1BxuX_JvQKLkceK3CqtO_znqFPvsSkS9Fxr-dV5nDeFud-uttczh0xYO6A7K8_paMQ5Yjr1uRlfWrHXnm9bYiJM4OLjbJ0fLaB-j1HENo4XFfkbLhIpY5CvsPgEdzcIw1qV2y--zQqJFoEoBu1yn-IaomZ--ROMZ2oepy4tgW7JUcrJfYP9q9B5gkjIL8OPn0VVOah3EGEkNoxfizj_kvY25awQ1QRj_lHnJPPOrC6RpI4ooCHmVrqhN2Cc-NyAm5jMZ6ozUe5xl0WgIt__KzfuFt2rlsRyw4frSYy9AqPR9SmWF0ixrPFTaO4BC_ulcqEqopaSrGrdlF5XqaeRJiFpKUyekkIMvw49-98h7K7hPcdnsSD44hP3vlDF7ZdbKzTMYSmxqqgYJp8N8bUVMl7xROcWu6cy71obuS8dJ9Ea3d77Z8bwRvBFpWnsPiW2GG5ds0i5eRa54Vvd5xEP3ielwSz0wHYBlz_D7_22HYcPMXsJU7m1QWw6dAsnfy4a51-fCgmFb_q5WnqlzD5fCGtRZ5lBB9uSIdltsxfaGQVG-JXFtJHqKPr0JZv1hHrWvXqZVQzlBpzrklIQSTURuouRXzd-Pi6OrJQ7vqtdenGuYhFExedHP88aEgyMT6Oer6hioS"

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