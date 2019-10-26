class PagesController < ApplicationController
  

  def interview
  	init = Preguntum.new
  	init.primera
  	cambio(init)
  end

  def cambio(init)
	#recibimos in
	case init.aasm_state # a_variable is the variable we want to compare
		when "b"    #compare to 1
			render "primera.html.erb",:locals => {:foo => "Esta es la pregunta"}	  		 
	  	
		else
	  		puts "it was something else"
	end	
  		
  end

end
