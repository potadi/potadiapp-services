from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from .services import predict_disease_saved_model

router = APIRouter(prefix='/api/diagnose')
    
@router.post('')
async def post(image: UploadFile = File(...)):
    """
    Diagnose the uploaded image.
    :param image: The image to be diagnosed.
    :return: The diagnosis result.
    """
    
    try:
        image_data = await image.read()
    except Exception as e:
        response = {
            'status': 'error',
            'message': f'Error while reading the image: {e}'
        }
        return JSONResponse(content=response, status_code=400)
    
    detection_result = predict_disease_saved_model(image_data, version=1)
    response = {
        'label': detection_result['label'],
        'confidence': detection_result['confidence'],
        'details': detection_result['probabilities']
    }
    
    return JSONResponse(content=response, status_code=200)
    