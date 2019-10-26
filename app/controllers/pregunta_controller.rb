class PreguntaController < ApplicationController


  # GET /pregunta
  # GET /pregunta.json
  def index
    @pregunta = Preguntum.all
  end

  # GET /pregunta/1
  # GET /pregunta/1.json
  def show
  end

  # GET /pregunta/new
  def new
    @preguntum = Preguntum.new
  end

  # GET /pregunta/1/edit
  def edit
  end

  # POST /pregunta
  # POST /pregunta.json
  def create
    @preguntum = Preguntum.new(preguntum_params)

    respond_to do |format|
      if @preguntum.save
        format.html { redirect_to @preguntum, notice: 'Preguntum was successfully created.' }
        format.json { render :show, status: :created, location: @preguntum }
      else
        format.html { render :new }
        format.json { render json: @preguntum.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /pregunta/1
  # PATCH/PUT /pregunta/1.json
  def update
    respond_to do |format|
      if @preguntum.update(preguntum_params)
        format.html { redirect_to @preguntum, notice: 'Preguntum was successfully updated.' }
        format.json { render :show, status: :ok, location: @preguntum }
      else
        format.html { render :edit }
        format.json { render json: @preguntum.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /pregunta/1
  # DELETE /pregunta/1.json
  def destroy
    @preguntum.destroy
    respond_to do |format|
      format.html { redirect_to pregunta_url, notice: 'Preguntum was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_preguntum
      @preguntum = Preguntum.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def preguntum_params
      params.require(:preguntum).permit(:name, :aasm_state)
    end
end
