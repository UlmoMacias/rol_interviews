class CreatePregunta < ActiveRecord::Migration[5.2]
  def change
    create_table :pregunta do |t|
      t.string :name
      t.string :aasm_state

      t.timestamps
    end
  end
end
