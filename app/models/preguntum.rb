require 'aasm'
class Preguntum < ApplicationRecord
  	include AASM
   		

  	aasm do
    	state :a, initial: true
    	state :b,:ba,:baa,:baaa,:baab,:baac,:baaba,:baabb

    event :primera do
      transitions from: :a, to: :b
    end

    event :segundo do
      transitions from: :b, to: :ba
    end   
  end
end