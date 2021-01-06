FROM kaggle/python

# our instrumentation uses astunparse sometimes
#RUN pip install astunparse


# install an older version of sklearn
# a lot of these scripts won't run with the latest and greatest
#RUN pip install scikit-learn==0.18


# use environment.yml to create conda env
ADD environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml

RUN echo "conda activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" >> ~/.bashrc
#ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH



EXPOSE 5000

ENV CONDA_DEFAULT_ENV $(head -1 /tmp/environment.yml | cut -d' ' -f2)
