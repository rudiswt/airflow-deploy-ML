PGDMP     %                    z            efishery    14.5    14.5     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24710    efishery    DATABASE     l   CREATE DATABASE efishery WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE efishery;
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                postgres    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   postgres    false    3            �            1259    24712    table_input    TABLE     �   CREATE TABLE public.table_input (
    id character varying NOT NULL,
    sepal_length real NOT NULL,
    sepal_width real NOT NULL,
    petal_length real NOT NULL,
    petal_width real NOT NULL
);
    DROP TABLE public.table_input;
       public         heap    postgres    false    3            �            1259    24711    table_input_id_seq    SEQUENCE     �   CREATE SEQUENCE public.table_input_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.table_input_id_seq;
       public          postgres    false    210    3            �           0    0    table_input_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.table_input_id_seq OWNED BY public.table_input.id;
          public          postgres    false    209            �            1259    24726    table_output    TABLE     �   CREATE TABLE public.table_output (
    id character varying NOT NULL,
    class smallint NOT NULL,
    executed_at timestamp with time zone
);
     DROP TABLE public.table_output;
       public         heap    postgres    false    3            �          0    24712    table_input 
   TABLE DATA                 public          postgres    false    210          �          0    24726    table_output 
   TABLE DATA                 public          postgres    false    211   �       �           0    0    table_input_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.table_input_id_seq', 1, false);
          public          postgres    false    209            a           2606    24737    table_input table_input_pk 
   CONSTRAINT     X   ALTER TABLE ONLY public.table_input
    ADD CONSTRAINT table_input_pk PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.table_input DROP CONSTRAINT table_input_pk;
       public            postgres    false    210            b           2606    24738    table_output table_output_fk    FK CONSTRAINT     |   ALTER TABLE ONLY public.table_output
    ADD CONSTRAINT table_output_fk FOREIGN KEY (id) REFERENCES public.table_input(id);
 F   ALTER TABLE ONLY public.table_output DROP CONSTRAINT table_output_fk;
       public          postgres    false    3169    211    210            �   ]   x���v
Q���W((M��L�+IL�I���+(-Qs�	uV�P7T�Q0�3�Q0�3�Q0��L5��<�4�H���MG�X�LG�P�h  ��"�      �   �  x����JCA��}��]�vH2��+]���nŊ�`��;k��>�{�$7��~�|���)�����G��O�o����z	��/�}��xZY�IHdE����E�Yb��T�M����_�2�%Z�]URC:����q���h��j-Ю}D��*�}DӑSV���hw=�8�k��=�c7��yf��k���"�=�@Ct�EsŦ�!��;����������0�c�Z�W���8�#����%Z���F:�����"I���7�r䔘q9���c�V7�n��Xǝ���Urލn�#�R�v��qMGℜj/�rlZzv�%�;J�*J���-G�L
u��S�{�!��K�w�1i-���M�i�(� }D�q�����E\,~ 2W�     