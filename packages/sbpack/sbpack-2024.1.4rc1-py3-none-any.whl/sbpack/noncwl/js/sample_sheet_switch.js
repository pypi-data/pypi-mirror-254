{
    if (INPUT_FILES_PORT) {
        return 'SAMPLE_SHEET_NAME';
    } else if (!INPUT_FILES_PORT && INPUT_SAMPLE_SHEET){
        return INPUT_SAMPLE_SHEET;
    } else {
        return "";
    }
}