Rails.application.routes.draw do
  resources :pregunta
  get 'pages/interview'
  get 'pages/myUpdate'
  get 'pregunta/primera'
  root to: redirect('/pages/interview')
  
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
