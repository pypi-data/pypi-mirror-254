depends = ('ITKPyBase', 'ITKTransform', 'ITKRegistrationMethodsv4', 'ITKImageLabel', 'ITKImageGrid', 'ITKIOTransformBase', 'ITKIOImageBase', 'ITKCommon', 'ITKBinaryMathematicalMorphology', )
templates = (  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationISS4ISS4', True, 'itk::Image< signed short,4 >, itk::Image< signed short,4 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationIUC4IUC4', True, 'itk::Image< unsigned char,4 >, itk::Image< unsigned char,4 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationIUS4IUS4', True, 'itk::Image< unsigned short,4 >, itk::Image< unsigned short,4 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationIF4IF4', True, 'itk::Image< float,4 >, itk::Image< float,4 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('ANTSRegistration', 'itk::ANTSRegistration', 'itkANTSRegistrationID4ID4', True, 'itk::Image< double,4 >, itk::Image< double,4 >'),
)
factories = ()
