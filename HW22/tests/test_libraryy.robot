*** Settings ***
Library    C:/Users/User/PycharmProjects/HWK-S/HW22/source/libraryy.py


*** Variables ***
${BOOK_NAME}    The Hobbit
${AUTHOR}       J.R.R. Tolkien
${NUM_PAGES}    400
${ISBN}         0006754023
${READER_NAME}  Vasya

*** Keywords ***
Create Book
    [Arguments]    ${book_name}    ${author}    ${num_pages}    ${isbn}
    ${book}=    Evaluate    libraryy.Book("${book_name}", "${author}", ${num_pages}, "${isbn}")    modules=libraryy
    RETURN    ${book}

Create Reader
    [Arguments]    ${name}
    ${reader}=    Evaluate    libraryy.Reader("${name}")    modules=libraryy
    RETURN    ${reader}

Reserve Book
    [Arguments]    ${reader}    ${book}
    ${result}=    Call Method    ${book}    reserve    ${reader}
    Log    ${result}
    RETURN    ${result}

Cancel Reservation
    [Arguments]    ${reader}    ${book}
    ${result}=    Call Method    ${book}    cancel_reserve    ${reader}
    Log    ${result}
    RETURN    ${result}

Get Book
    [Arguments]    ${reader}    ${book}
    ${result}=    Call Method    ${book}    get_book    ${reader}
    Log    ${result}
    RETURN    ${result}

Return Book
    [Arguments]    ${reader}    ${book}
    ${result}=    Call Method    ${book}    return_book    ${reader}
    Log    ${result}
    RETURN    ${result}

*** Test Cases ***
Test Create Book
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${NUM_PAGES}    ${ISBN}
    SHOULD BE EQUAL    ${book.book_name}    ${BOOK_NAME}
    SHOULD BE EQUAL    ${book.author}       ${AUTHOR}
    SHOULD BE EQUAL AS NUMBERS    ${book.num_pages}    ${NUM_PAGES}
    SHOULD BE EQUAL    ${book.isbn}         ${ISBN}

Test Create Reader
    ${reader}=    Create Reader    ${READER_NAME}
    SHOULD BE EQUAL    ${reader.name}    ${READER_NAME}

Test Reserve Book
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${NUM_PAGES}    ${ISBN}
    ${reader}=    Create Reader    ${READER_NAME}
    ${result}=    Reserve Book    ${reader}    ${book}
    SHOULD BE EQUAL    ${result}    Книга ${BOOK_NAME} зарезервирована за ${READER_NAME}

Test Cancel Reservation
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${NUM_PAGES}    ${ISBN}
    ${reader}=    Create Reader    ${READER_NAME}
    ${reserve}=   Reserve Book    ${reader}    ${book}
    ${result}=    Cancel Reservation    ${reader}    ${book}
    SHOULD BE EQUAL    ${result}    Резервация на книгу ${BOOK_NAME} отменена

Test Get Book
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${NUM_PAGES}    ${ISBN}
    ${reader}=    Create Reader    ${READER_NAME}
    ${reserve}=    Reserve Book    ${reader}    ${book}
    ${result}=    Get Book    ${reader}    ${book}
    SHOULD BE EQUAL    ${result}    Книга ${BOOK_NAME} выдана ${READER_NAME}

Test Return Book
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${NUM_PAGES}    ${ISBN}
    ${reader}=    Create Reader    ${READER_NAME}
    ${reserve}=   Reserve Book    ${reader}    ${book}
    ${issued}=    Get Book    ${reader}    ${book}
    ${result}=    Return Book    ${reader}    ${book}
    SHOULD BE EQUAL    ${result}    Книга ${BOOK_NAME} возвращена ${READER_NAME}

Test Duplicate Reservation (Expected Failure)
    ${book}=     Create Book    ${BOOK_NAME}    ${AUTHOR}    ${NUM_PAGES}    ${ISBN}
    ${reader}=   Create Reader  ${READER_NAME}
    Reserve Book   ${reader}    ${book}
    ${expected}=   Set Variable    Calling method 'reserve' failed: Книга уже заревервирована
    Run Keyword And Expect Error    ${expected}    Reserve Book    ${reader}    ${book}
