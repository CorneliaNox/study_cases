def test_upload_file():
  # Arrange
  admin = admin_scenario.create_admin()
  session = session_scenario.create_session(admin)

  program = program_scenario.create_program(session=session)

  xlsx = mentor_upload_steps.create_xlsx()

  rabbitmq = RabbitMqMockService()
  rabbitmq.mock_message_response(correlation_id="123", response={no_ack:true})

  # Act
  response = program_admin_scenario.upload_mentors(program=program, xlsx=xlsx, session=session)

  # Assert
  file =  s3.get_file(response.data.task.metadata.file_path)

  assert file is not None
  assert file.mediatype == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"





class RabbitMqMockService:
  def __init__(self, url: str):
    self.url = url

  def mock_message_response(self, correlation_id, response):
    requests.post(self.url, json={
      "correlation_id": correlation_id,
      "response": response
    })