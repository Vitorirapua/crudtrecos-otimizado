from flask import g, redirect, render_template, request, url_for

from functions.db_usuario import update_perfil_usuario, update_senha


def mod_editaperfil(mysql):

    # Se o usuário não está logado redireciona para a página de login
    if g.usuario == '':
        return redirect(url_for('login'))

    if request.method == 'POST':

        form = dict(request.form)

        # print('\n\n\n FORM:', form, '\n\n\n')

        update_perfil_usuario(mysql=mysql, form=form)

        # Se pediu para trocar a senha
        if form['senha2'] != '':

            update_senha(mysql=mysql)

        return redirect(url_for('logout'))
############
    # Recebe dados do usuário
    sql = '''
        SELECT * FROM usuario
        WHERE u_id = %s
            AND u_status = 'on'    
    '''
    cur = mysql.connection.cursor()
    cur.execute(sql, (g.usuario['id'],))
    row = cur.fetchone()
    cur.close()
#############
    # print('\n\n\n USER:', row, '\n\n\n')

    pagina = {
        'titulo': 'CRUDTrecos - Erro 404',
        'usuario': g.usuario,
        'form': row
    }
    return render_template('editaperfil.html', **pagina)