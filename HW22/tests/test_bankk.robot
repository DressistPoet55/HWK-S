*** Settings ***
Library    C:/Users/User/PycharmProjects/HWK-S/HW22/source/bankk.py

*** Variables ***
${interest_rate}    0.10
${client_id}        0000001
${name}             Stepan
${start_balance}    1000
${years}            1

*** Keywords ***
Initialize bank
    ${bank}=    Create Bank
    RETURN    ${bank}

Initialize deposit
    ${deposit}=    Create Deposit    ${start_balance}    ${years}    ${interest_rate}
    RETURN    ${deposit}

Register Client
    [Arguments]    ${bank}    ${client_id}    ${name}
    ${result}=    Call Method    ${bank}    register_client    ${client_id}    ${name}
    Log    ${result}
    RETURN    ${result}

Open Deposit Account
    [Arguments]    ${bank}    ${client_id}    ${start_balance}    ${years}
    ${result}=    Call Method    ${bank}    open_deposit_account    ${client_id}    ${start_balance}    ${years}
    Log    ${result}
    RETURN    ${result}

Calculate Deposit Interest Rate
    [Arguments]    ${bank}    ${client_id}
    ${result}=    Call Method    ${bank}    calc_deposit_interest_rate    ${client_id}
    Log    ${result}
    RETURN    ${result}

Close Deposit Account
    [Arguments]    ${bank}    ${client_id}
    ${result}=    Call Method    ${bank}    close_deposit    ${client_id}
    Log    ${result}
    RETURN    ${result}

*** Test Cases ***
Test Register Client
    ${bank}=    Initialize Bank
    ${result}=  Register Client    ${bank}    ${client_id}    ${name}
    SHOULD BE EQUAL    ${result}    Зарегистрирован клиент по имени ${name} , и присвоен личный id ${client_id}

Test Register Duplicate Client (Expected Failure)
    [Tags]    expected_fail
    ${bank}=    Initialize Bank
    ${result1}=    Register Client    ${bank}    ${client_id}    Vasya
    ${result2}=    Register Client    ${bank}    ${client_id}    Vasya
    SHOULD BE EQUAL    ${result2}    Клиент с ID ${client_id} уже существует

Test Open Deposit
    ${bank}=    Initialize Bank
    Register Client    ${bank}    ${client_id}    ${name}
    ${result}=  Open Deposit Account    ${bank}    ${client_id}    ${start_balance}    ${years}
    SHOULD BE EQUAL    ${result}    Открыт депозитный счет по id: ${client_id}, с балансом ${start_balance} рублей на ${years} лет

Test Calculate Deposit Interest Rate
    ${bank}=    Initialize Bank
    Register Client    ${bank}    ${client_id}    ${name}
    Open Deposit Account    ${bank}    ${client_id}    ${start_balance}    ${years}
    ${result}=  Calculate Deposit Interest Rate    ${bank}    ${client_id}
    SHOULD BE EQUAL AS NUMBERS    ${result}    1104.7130674412967

Test Close Deposit Account
    ${bank}=    Initialize Bank
    Register Client    ${bank}    ${client_id}    ${name}
    Open Deposit Account    ${bank}    ${client_id}    ${start_balance}    ${years}
    ${result}=  Close Deposit Account    ${bank}    ${client_id}
    SHOULD BE EQUAL    ${result}    Депозитный счет закрыт
