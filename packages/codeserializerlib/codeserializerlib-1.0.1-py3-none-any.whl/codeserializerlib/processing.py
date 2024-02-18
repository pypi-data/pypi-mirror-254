import spacy
import os
from codeserializerlib.models.code import code
from codeserializerlib.models.code_type import code_type
from codeserializerlib.models.label import label


# only export the process_message function
__all__ = ['process_message']

def process_message(shopName: str, message: str) -> list[code]:
    current_script_path = os.path.dirname(os.path.realpath(__file__))
    model_path = os.path.join(current_script_path, "model")

    nlp = spacy.load(model_path)

    doc = nlp(message)

    print ("Entities", [(ent.text, ent.label_) for ent in doc.ents])

    credit_codes = extract_credit_codes(shopName, doc)
    percentage_codes = extract_percentage_codes(shopName, doc)
    free_shipping_codes = extract_freeshipping_codes(shopName, doc)
    early_access_codes = extract_earlyaccess_codes(shopName, doc)

    codes = credit_codes + percentage_codes + free_shipping_codes + early_access_codes

    return codes


def extract_credit_codes(shopName: str, document) -> list[code]:
    creditCodes = []

    for entity in document.ents:
        if entity.label_ == label.credit_code.value:
            creditAmount = None
            minSpendAmount = None

            for potentialCredit in document.ents:
                if potentialCredit.label_ == label.credit_amount.value:
                    # Remove all non-digits from the string (€, $, etc.)
                    creditAmount = int(''.join(filter(str.isdigit, potentialCredit.text)))
                    break

            for potentialMinSpend in document.ents:
                if potentialMinSpend.label_ == label.minimum_order_value.value:
                    # Remove all non-digits from the string (€, $, etc.)
                    minSpendAmount = int(''.join(filter(str.isdigit, potentialMinSpend.text)))
                    break

            appendCode = code(hash=entity.text,
                        code_type=code_type.store_credit,
                        shop_name=shopName,
                        value=creditAmount,
                        min_spend=minSpendAmount)

            creditCodes.append(appendCode)

    return creditCodes


def extract_percentage_codes(shopName: str, document) -> list[code]:
    percentage_codes = []

    for entity in document.ents:
        if entity.label_ == label.percentage_code.value:
            percentage_value = None
            minSpendAmount = None

            for potential_percentage in document.ents:
                if potential_percentage.label_ == label.percentage.value:
                    percentage_value = potential_percentage.text
                    break

            for potentialMinSpend in document.ents:
                if potentialMinSpend.label_ == label.minimum_order_value.value:
                    # Remove all non-digits from the string (€, $, etc.)
                    minSpendAmount = int(''.join(filter(str.isdigit, potentialMinSpend.text)))
                    break

            appendCode = code(
                hash=entity.text,
                code_type=code_type.discount,
                shop_name=shopName,
                value=percentage_value,
                min_spend=minSpendAmount)

            percentage_codes.append(appendCode)

    return percentage_codes

    
def extract_freeshipping_codes(shopName: str, document) -> list[code]:
    free_shipping_codes = []

    for entity in document.ents:
        if entity.label_ == label.free_shipping_code.value:
            minSpendAmount = None

            for potentialMinSpend in document.ents:
                if potentialMinSpend.label_ == label.minimum_order_value.value:
                    # Remove all non-digits from the string (€, $, etc.)
                    minSpendAmount = int(''.join(filter(str.isdigit, potentialMinSpend.text)))
                    break

            appendCode = code(
                hash=entity.text,
                code_type=code_type.free_shipping,
                shop_name=shopName,
                min_spend=minSpendAmount)

            # Append the Code object to the list
            free_shipping_codes.append(appendCode)

    return free_shipping_codes


def extract_earlyaccess_codes(shopName: str, document) -> list[code]:
    early_access_codes = []

    for entity in document.ents:
        if entity.label_ == label.early_access_code.value:
            appendCode = code(
                hash=entity.text,
                code_type=code_type.early_access,
                shop_name=shopName)

            # Append the Code object to the list
            early_access_codes.append(appendCode)

    return early_access_codes
