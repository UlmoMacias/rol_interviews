require 'test_helper'

class PagesControllerTest < ActionDispatch::IntegrationTest
  test "should get interview" do
    get pages_interview_url
    assert_response :success
  end

end
